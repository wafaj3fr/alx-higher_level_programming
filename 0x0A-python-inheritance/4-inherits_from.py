#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """Method returns True if an object is an instance of a class"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
