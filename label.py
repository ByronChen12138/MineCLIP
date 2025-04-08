import datetime

from main.mineclip.action_predictor import ActionPredictor
from utils.json_utils import append_jsonl


VIDEO_ID = "0VfvCDDPHyw"
VIDEO_START_TIME = 75  # seconds
VIDEO_DURATION = 6  # seconds


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


def main():
    # Get the current time
    start_time = datetime.datetime.now()

    action_predictor = ActionPredictor(
        config_path = "./config",
        labels_path = "./labels.txt",
        encoded_labels_path = "./labels_features.pt"
    )

    label_video(
        action_predictor = action_predictor,
        video_id = VIDEO_ID,
        start_time = VIDEO_START_TIME,
        duration = VIDEO_DURATION,
        video_height = 160,
        video_width = 256,
        top_k = 5,
        is_print = False,
        out_file = "./outs/labels.jsonl"
    )

    # Print the time taken
    end_time = datetime.datetime.now()
    taken_time = end_time - start_time
    print(f"Time taken: {taken_time}")


if __name__ == "__main__":
    main()