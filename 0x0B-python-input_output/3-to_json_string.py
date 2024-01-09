#!/usr/bin/python3
"""to_json_string function"""


import json


def to_json_string(my_obj):
    """Returns th JSON representation of my_obj.

    Args:
        - my_obj: string to represent

    Returns: JSON representation
    """

    return json.dumps(my_obj)
