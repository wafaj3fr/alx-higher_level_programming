#!/usr/bin/python3
"""class LockedClass"""


class LockedClass:
    """
    Locked Class
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """new instances of Locked Class."""
        self.first_name = "first_name"
