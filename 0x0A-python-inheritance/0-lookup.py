#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    # Use dir() to get the list of names
    names = dir(obj)

    # Filter out attributes and methods that are not callable
    result = [name for name in names if callable(getattr(obj, name))]

    return result
