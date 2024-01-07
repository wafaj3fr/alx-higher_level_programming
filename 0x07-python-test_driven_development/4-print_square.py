#!/usr/bin/python3
""" print square function """


def print_square(size):
    """
    Print a square with the character #.

    Parameters:
    - size (int): The size length of the square.

    Returns:
    None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float):
        raise TypeError("size must be an integer")

    # Print the square
    for _ in range(size):
        print("#" * size)
