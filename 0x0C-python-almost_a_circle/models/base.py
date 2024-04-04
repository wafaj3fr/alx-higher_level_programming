#!/usr/bin/python3
"""Base class"""


class Base():
    """
    Base class for managing id attributes in other classes.

    Attributes:
        __nb_objects (int): Private attribute to keep track of objects.
        id (int): Public attribute representing the identifier.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): The identifier for the instance.
                If id is not provided, it will be automatically generated.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
