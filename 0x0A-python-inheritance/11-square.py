#!/usr/bin/python3
"""
 Square class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square. Inherits from Rectangle.
    attribute size.
    method area().
    """

    def __init__(self, size):
        """Initializes a Square.

        Args:
            - size: size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Calculates the area of a Square instance.
        """

        return self.__size ** 2
