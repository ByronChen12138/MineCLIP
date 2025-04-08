from __future__ import annotations

import os

def read_txt(file_path: str) -> list:
    """
    Read a list of strings from a text file
    :param file_path: The path to the file
    :return: List of strings
    """
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def write_txt(file_path: str, input: str) -> None:
    """
    Write a list of strings to a text file
    :param file_path: The path to the file
    :param input: Strings
    :return: None
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w') as f:
        f.write(input)


def append_txt(file_path: str, input: str) -> None:
    """
    Append a list of strings to a text file, one string per line.
    Creates the file and parent directories if they do not exist.

    :param file_path: The path to the text file.
    :param input: Strings
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Append data
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(input + '\n')