#!/usr/bin/python3
"""student class"""


class Student:
    """Class that defines a student.
    Public attributes:
        - first_name
        - last_name
        - age
    Public method to_json().
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation
        of a Student instance.

        Returns: the dict representation of the instance.
        """

        return self.__dict__
    """Creates a dict description of obj.

        Args:
            - obj: object to serialize

        Returns: dictionnary description of obj
        """

        return obj.__dict__
