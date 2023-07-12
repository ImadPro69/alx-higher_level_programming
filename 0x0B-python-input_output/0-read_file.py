#!/usr/bin/python3
"""0-read_file.py"""

def read_file(filename=""):
    """
    Reads a text file and prints its contents
    """
    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.read()
        print(contents, end='')
