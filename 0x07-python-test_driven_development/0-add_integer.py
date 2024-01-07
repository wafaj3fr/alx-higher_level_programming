#!/usr/bin/python3
""" Addition function """


def add_integer(a, b=98):
    """
    This function adds two integers.

    Parameters:
    - a (int): The first integer.
    - b (int): The second integer. Default is 98.

    Returns:
    int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)
    return a + b
