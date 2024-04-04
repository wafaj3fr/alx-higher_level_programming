#!/usr/bin/python3
"""Base class"""

class Base():
    """
    Base class for managing id attributes in other classes.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of the number of objects created.
        id (int): Public instance attribute representing the unique identifier of an instance.
        
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): The unique identifier for the instance. Defaults to None.
                If id is not provided, it will be automatically generated.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
