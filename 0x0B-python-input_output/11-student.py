#!/usr/bin/python3
"""student class"""


class Student:
    """student class.
    Public attributes:
         first_name, last_name, age.
    Public method to_json().
    Public method reload_from_json().
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, ar=None):
        """Retrieves a dictionary representation
        of a Student instance.

        Args:
            - ar: list of attributes

        Returns: the dict representation of the instance.
        """

        my_dict = dict()
        if ar and all(isinstance(x, str) for x in ar):
            for x in ar:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            - json: dictionnary of attributes
        """

        for x in json:
            self.__dict__.update({x: json[x]})
