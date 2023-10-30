#!/usr/bin/python3
"""Reactangle Module"""


class Rectangle:
    """creates a Reactangle"""

    def __init__(self, width=0, height=0):
        """create instances for a rectangle

        Args:
            width (int, optional): width. Defaults to 0.
            height (int, optional): hight. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        return ((self.__height + self.__width) * 2)
