#!/usr/bin/python3
"""
BaseGeometry inherited module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherited class"""

    def __init__(self, width, height):
        """class initialization"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method calculating area"""

        return self.__width * self__.height

    def __str__(self):
        """Method to return string representation"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
