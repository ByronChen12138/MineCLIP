from __future__ import annotations

import json
import os

from typing import List, Dict


def read_json(file_path: str) -> list:
    """
    Read a list of json objects from a file
    :param file_path: The path to the file
    :return: List of json objects
    """
    with open(file_path, 'r') as f:
        return json.load(f)


def write_json(file_path: str, data: list | dict) -> None:
    """
    Write a list of json objects to a file
    :param file_path: The path to the file
    :param data: The list of json objects
    :return: None
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def read_jsonl(file_path: str) -> list:
    """
    Read a list of json objects from a file
    :param file_path: The path to the file
    :return: List of json objects
    """
    with open(file_path, 'r') as f:
        return [json.loads(line) for line in f]


def append_jsonl(file_path: str, data: List[Dict]) -> None:
    """
    Append a list of JSON objects to a .jsonl file, one JSON object per line.
    Creates the file and parent directories if they do not exist.

    :param file_path: The path to the .jsonl file.
    :param data: A list of JSON-serializable dictionaries.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Append data
    with open(file_path, 'a', encoding='utf-8') as f:
        for item in data:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')

