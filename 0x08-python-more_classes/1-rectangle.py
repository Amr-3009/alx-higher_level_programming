#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """Rectangle class

    Args:
        width (int): horizontal dimesion of rectangle, default is 1
        height (int): vertical dimesion of rectangle, default is 1
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter

        Returns:
            __width (int): hor dim

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): val of width

        Attributes:
            __width (int): horizontal dimesion

        Raises:
            TypeError: if 'value' is not int
            ValueError: if 'value' is less than 0

        """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be greater than 0')
        self.__width = value

    @property
    def height(self):
        """__height getter

        Returns:
            __height (int): ver dim

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): val of height

        Attributes:
            __height (int): vertical dimesion

        Raises:
            TypeError: if 'value' is not int
            ValueError: if 'value' is less than 0

        """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be greater than 0')
        self.__height = value
