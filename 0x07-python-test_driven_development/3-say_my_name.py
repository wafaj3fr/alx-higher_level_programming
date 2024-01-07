#!/usr/bin/python3
""" name function """


def say_my_name(first_name, last_name=""):
    """
    Print a message with the given first name and last name.

    Parameters:
    - first_name (str): The first name.
    - last_name (str, optional): The last name. Default is an empty string.

    Returns:
    None
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the message
    full_name = f"My name is {first_name} {last_name}"
    print(full_name)
