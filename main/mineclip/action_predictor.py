import os

import cv2
import torch
import numpy as np
import hydra
import hashlib

from omegaconf import OmegaConf
from mineclip import MineCLIP


def load_video_clip(
        filepath: str,
        start_time_sec: int,
        duration_sec: int = 16,
        height: int =160, width: int =256
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
        A tensor of shape (1, 16, 3, height, width).
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

    # Convert to tensor (16, 3, 160, 256)
    video_tensor = torch.tensor(np.stack(frames)).permute(0, 3, 1, 2).float()

    # Add batch dimension (1, 16, 3, 160, 256)
    video_tensor = video_tensor.unsqueeze(0)
    return video_tensor


@torch.no_grad()
@hydra.main(config_name="conf", config_path=".", version_base="1.1")
def main(cfg):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    OmegaConf.set_struct(cfg, False)
    ckpt = cfg.pop("ckpt")
    OmegaConf.set_struct(cfg, True)

    # Print current directory
    print(f"Current working directory: {os.getcwd()}")

    assert (
        hashlib.md5(open(ckpt.path, "rb").read()).hexdigest() == ckpt.checksum
    ), "broken ckpt"

    model = MineCLIP(**cfg).to(device)
    model.load_ckpt(ckpt.path, strict=True)
    print("Successfully loaded ckpt")

    video = load_video_clip("/Users/nosanq/Desktop/McGill/Graduated Study/MIMIC/MIMIC v2.0 2025.3/Codes/Mimicking/downloads/0VfvCDDPHyw.mp4")

    prompts = [
        "Mining",
        "Attacking",
        "Crafting",
        "Swimming",
    ]

    VIDEO_BATCH, TEXT_BATCH = video.size(0), len(prompts)

    image_feats = model.forward_image_features(video)
    video_feats = model.forward_video_features(image_feats)
    assert video_feats.shape == (VIDEO_BATCH, 512)
    video_feats_2 = model.encode_video(video)
    # encode_video is equivalent to forward_video_features(forward_image_features(video))
    torch.testing.assert_close(video_feats, video_feats_2)

    # encode batch of prompts
    text_feats_batch = model.encode_text(prompts)
    assert text_feats_batch.shape == (TEXT_BATCH, 512)

    # compute reward from features
    logits_per_video, logits_per_text = model.forward_reward_head(
        video_feats, text_tokens=text_feats_batch
    )
    assert logits_per_video.shape == (VIDEO_BATCH, TEXT_BATCH)
    assert logits_per_text.shape == (TEXT_BATCH, VIDEO_BATCH)
    # directly pass in strings. This invokes the tokenizer under the hood
    reward_scores_2, _ = model.forward_reward_head(video_feats, text_tokens=prompts)
    # pass in cached, encoded text features
    reward_scores_3, _ = model(
        video_feats, text_tokens=text_feats_batch, is_video_features=True
    )
    reward_scores_4, _ = model(
        video, text_tokens=text_feats_batch, is_video_features=False
    )
    # all above are equivalent, just starting from features or raw values
    torch.testing.assert_close(logits_per_video, reward_scores_2)
    torch.testing.assert_close(logits_per_video, reward_scores_3)
    torch.testing.assert_close(logits_per_video, reward_scores_4)

    print("Inference successful")

    print(f"The logits per video are {logits_per_video}")
    # print(f"The logits per text are {logits_per_text}")

    # Output the prompts with the logits in descending order
    sorted_indices = torch.argsort(logits_per_video[0], descending=True)
    sorted_prompts = [prompts[i] for i in sorted_indices]
    sorted_logits = [logits_per_video[0][i].item() for i in sorted_indices]

    for prompt, logit in zip(sorted_prompts, sorted_logits):
        print(f"{prompt}: {logit}")


if __name__ == "__main__":
    main()
