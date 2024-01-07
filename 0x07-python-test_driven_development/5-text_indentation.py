#!/usr/bin/python3
""" text indentation """


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?', and ':'.

    Parameters:
    - text (str): The input text.

    Returns:
    None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ""

    for char in text:
        current_line += char

        if char in ['.', '?', ':']:
            print(current_line.strip())

            print("\n\n")

            current_line = ""

    if current_line:
        print(current_line.strip())
