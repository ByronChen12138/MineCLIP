from main.mineclip.action_predictor import ActionPredictor
from utils.json_utils import append_jsonl

VIDEO_ID = "0VfvCDDPHyw"
VIDEO_START_TIME = 75  # seconds
VIDEO_DURATION = 6  # seconds

def main():
    action_predictor = ActionPredictor(
        config_path = "./config",
        labels_path = "./labels.txt"
    )

    video = action_predictor.load_video_clip(
        filepath = f'./downloads/{VIDEO_ID}.mp4',
        start_time_sec = VIDEO_START_TIME,
        duration_sec = VIDEO_DURATION,
        height = 160,
        width = 256
    )

    labels = action_predictor.predict_action(video)
    print(labels)

    # Create a dictionary to store the labels and the video path
    label_dict = {
        "video_id": VIDEO_ID,
        "video_start_time": VIDEO_START_TIME,
        "video_duration": VIDEO_DURATION,
        "labels": labels
    }

    # Store the label_dict in a jsonl file
    append_jsonl(
        file_path = "./outs/labels.jsonl",
        data = [label_dict]
    )

if __name__ == "__main__":
    main()