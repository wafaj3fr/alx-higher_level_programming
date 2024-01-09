#!/usr/bin/python3
"""save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """Writes the representation of my_obj
    to filename.

    Args:
        - my_obj: object to write
        - filename: file to write into
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
