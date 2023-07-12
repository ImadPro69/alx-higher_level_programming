#!/usr/bin/python3
"""0-read_file.py"""

def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read (default is an empty string).

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.read()
        print(contents, end='')


if __name__ == "__main__":
    read_file()

