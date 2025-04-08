import os

import cv2
import torch
import numpy as np
import hashlib

from omegaconf import OmegaConf
from mineclip import MineCLIP


class ActionPredictor:
    def __init__(
            self,
            config_path: str = "./conf",
            labels_path: str = "./labels.txt"
    ):
        """
        Initializes the ActionPredictor by loading the model configuration,
        checkpoint, and label mappings.

        Args:
            config_path (str): Directory containing the configuration YAML file.
            labels_path (str): Path to the labels file.
        """

        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        # elif torch.backends.mps.is_available():
        #     self.device = torch.device("mps")
        else:
            self.device = torch.device("cpu")

        print(f"Using device: {self.device}")

        # Load configuration
        cfg = OmegaConf.load(os.path.join(config_path, "conf.yaml"))
        OmegaConf.set_struct(cfg, False)
        ckpt = cfg.pop("ckpt")
        OmegaConf.set_struct(cfg, True)

        # Validate checkpoint
        if not isinstance(ckpt.path, str) or not os.path.isfile(ckpt.path):
            raise FileNotFoundError(f"Checkpoint path is invalid or not found: {ckpt.path}")

        # If checksum is provided in config, verify it
        if hasattr(ckpt.path, "checksum"):
            actual_checksum = hashlib.md5(open(ckpt.path, "rb").read()).hexdigest()
            if actual_checksum != ckpt.checksum:
                raise ValueError("Checkpoint file is corrupted or checksum mismatch.")

        # Load model
        self.model = MineCLIP(**cfg).to(self.device)
        self.model.load_ckpt(ckpt.path, strict=True)
        print("Successfully loaded checkpoint.")

        # Load label mappings
        self.labels_path = labels_path
        self.labels = self.load_labels()


    def load_labels(self):
        """
        Load labels from a text file.
        Returns:
            A list of labels.
        """
        with open(self.labels_path, "r") as f:
            labels = [line.strip() for line in f.readlines()]
        return labels


    def load_video_clip(
            self,
            filepath: str,
            start_time_sec: int,
            duration_sec: int = 16,
            height: int = 160, width: int = 256
    ):
        """
        Load a video clip from a file and convert it to a tensor.
        Args:
            filepath: Path to the video file.
            start_time_sec: Start time in seconds.
            duration_sec: Duration in seconds.
            height: Height of the output frames.
            width: Width of the output frames.

        Returns:
            A tensor of shape (1, duration_sec, 3, height, width).
        """
        end_time_sec = start_time_sec + duration_sec

        # Open the video file
        cap = cv2.VideoCapture(filepath)
        video_fps = cap.get(cv2.CAP_PROP_FPS)

        # Calculate frame indices to capture 1 frame per second
        frame_indices = [
            int((start_time_sec + i) * video_fps)
            for i in range(end_time_sec - start_time_sec)
        ]

        frames = []
        for idx in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if not ret:
                raise ValueError(f"Frame at index {idx} could not be read.")
            # BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Resize
            frame = cv2.resize(frame, (width, height))
            frames.append(frame)

        cap.release()

        # Convert to tensor (duration_sec, 3, 160, 256)
        video_tensor = torch.tensor(np.stack(frames)).permute(0, 3, 1, 2).float()

        # Add batch dimension (1, duration_sec, 3, 160, 256)
        video_tensor = video_tensor.unsqueeze(0)
        return video_tensor

    @torch.no_grad()
    def predict_action(
            self,
            video: torch.Tensor,
            top_k: int = 5,
            is_print: bool = False
    ):
        """
        Predict the action from a video tensor.
        Args:
            video: A tensor of shape (1, duration_sec, 3, height, width).
            top_k: Number of top actions to return.
            is_print: Whether to print the scores.

        Returns:
            The top k labels with their scores in descending order.
        """
        print(video.shape)

        video = video.to(self.device)
        image_feats = self.model.forward_image_features(video)
        video_feats = self.model.forward_video_features(image_feats)

        # print(video.device)
        # print(next(self.model.parameters()).device)

        # encode batch of prompts
        text_feats_batch = self.model.encode_text(self.labels)

        # compute reward from features
        scores_per_video, _ = self.model.forward_reward_head(
            video_feats, text_tokens=text_feats_batch
        )

        if is_print:
            print(f"The scores per video are {scores_per_video}")

        # Output the top k labels in descending order with their scores in a dictionary with float values
        scores_per_video = scores_per_video.squeeze(0).cpu().numpy()

        indices = np.argsort(scores_per_video)[::-1][:top_k]
        labels = [self.labels[i] for i in indices]
        scores = [float(scores_per_video[i]) for i in indices]  # Convert to Python float
        result = {labels[i]: scores[i] for i in range(top_k)}

        if is_print:
            print(f"The top {top_k} labels are {result}")

        return result