import datetime
import math

import cv2

from main.mineclip.action_predictor import ActionPredictor
from utils.json_utils import append_jsonl


VIDEO_ID = "9ioB_HaLD6s"
VIDEO_START_TIME = 0  # seconds
VIDEO_DURATIONS = [4, 6, 8, 10, 12, 14, 16]
OVERLAP_COEFFICIENTS = [0.1, 0.2, 0.3, 0.4, 0.5]


def label_video(
        action_predictor: ActionPredictor,
        video_id: str,
        start_time: int,
        duration: int,
        video_height: int = 160,
        video_width: int = 256,
        top_k: int = 5,
        is_print: bool = False,
        out_file: str = "./outs/labels.jsonl"
) -> dict:
    """
    Label a video using the ActionPredictor class.
    :param action_predictor: An instance of the ActionPredictor class.
    :param video_id: The ID of the video to label.
    :param start_time: The start time in seconds.
    :param duration: The duration in seconds.
    :param video_height: The height of the video frames.
    :param video_width: The width of the video frames.
    :param top_k: The number of top actions to return.
    :param is_print: Whether to print the labels.
    :param out_file: The output file path to store the labels.
    :return: A dictionary containing the video ID, start time, duration, and labels.
    """
    video = action_predictor.load_video_clip(
        filepath=f'./downloads/{video_id}.mp4',
        start_time_sec=start_time,
        duration_sec=duration,
        height=video_height,
        width=video_width
    )

    labels = action_predictor.predict_action(video, top_k, is_print)

    # Create a dictionary to store the labels and the video path
    label_dict = {
        "video_id": video_id,
        "video_start_time": start_time,
        "video_duration": duration,
        "labels": labels
    }

    print(label_dict)

    # Store the label_dict in a jsonl file
    append_jsonl(
        file_path=out_file,
        data=[label_dict]
    )

    return label_dict


def get_video_duration(video_path: str) -> float:
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    total_duration = frame_count / fps  # in seconds
    cap.release()

    return total_duration


def clip_video(
        video_total_duration: int,
        prev_start_time: int,
        duration: int,
        overlap_time: int
) -> tuple:
    """
    Clip the video to a new start time and duration.
    :param video_total_duration: The total duration of the video in seconds.
    :param prev_start_time: The previous start time in seconds.
    :param duration: The duration in seconds.
    :param overlap_time: The overlap time in seconds.
    :return: A tuple containing the new start time and duration.
    """
    new_start_time = prev_start_time + duration - overlap_time
    new_duration = min(video_total_duration - new_start_time, duration)
    return new_start_time, new_duration



def main():
    # Get the current time
    start_time = datetime.datetime.now()

    action_predictor = ActionPredictor(
        config_path = "./config",
        labels_path = "./labels.txt",
        encoded_labels_path = "./labels_features.pt"
    )

    # Get the total duration of the video
    video_total_duration = math.floor(get_video_duration(f'./downloads/{VIDEO_ID}.mp4'))
    print(f"Total duration of the video: {video_total_duration} seconds")

    for VIDEO_DURATION in VIDEO_DURATIONS:
        for OVERLAP_COEFFICIENT in OVERLAP_COEFFICIENTS:

            video_start_time = VIDEO_START_TIME
            video_duration = VIDEO_DURATION
            overlap_time = math.floor(VIDEO_DURATION * OVERLAP_COEFFICIENT)
            if overlap_time == 0:
                continue

            while True:
                label_video(
                    action_predictor=action_predictor,
                    video_id=VIDEO_ID,
                    start_time=video_start_time,
                    duration=video_duration,
                    video_height=160,
                    video_width=256,
                    top_k=5,
                    is_print=False,
                    out_file=f"./outs/labels/{VIDEO_ID}/d{VIDEO_DURATION}_o{OVERLAP_COEFFICIENT}.jsonl"
                )

                video_start_time, video_duration = clip_video(
                    video_total_duration=video_total_duration,
                    prev_start_time=video_start_time,
                    duration=VIDEO_DURATION,
                    overlap_time=overlap_time
                )

                # Check if the new start time exceeds the total duration
                if video_start_time >= video_total_duration:
                    break

    # Print the time taken
    end_time = datetime.datetime.now()
    taken_time = end_time - start_time
    print(f"Time taken: {taken_time}")


if __name__ == "__main__":
    main()