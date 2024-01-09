#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read(), end="")
