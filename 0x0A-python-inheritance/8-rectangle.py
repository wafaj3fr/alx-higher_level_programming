#!/usr/bin/python3
"""class Rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle. Inherits from BaseGeometry.
    attributes:
        - width
        - height
    """

    def __init__(self, width, height):
        """Initializes an instance.

        Args:
            - width: width of the rectangle
            - heigth: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
