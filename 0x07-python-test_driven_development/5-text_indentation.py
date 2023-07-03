#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':' characters.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text into sentences based on '.', '?', and ':' characters
    sentences = []
    current_sentence = ""
    for char in text:
        current_sentence += char
        if char in ['.', '?', ':']:
            sentences.append(current_sentence.strip())
            current_sentence = ""

    # Print the sentences with 2 new lines after each
    for sentence in sentences:
        print(sentence)
        print()

