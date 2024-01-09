#!/usr/bin/python3
"""append_write function"""


def append_write(filename="", text=""):
    """Appends text to filename.
    Args:
        - filename: name of the file
        - text: text to append
    Returns: the number of characters added
    """

    with open(filename, 'a+') as f:
        return f.write(text)
