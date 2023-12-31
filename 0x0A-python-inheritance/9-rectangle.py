#!/usr/bin/python3
"""module for alx task"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class for alx task
    """
    def __init__(self, width, height):
        """init method for height and width

        Args:
            width (int): first arguemnt
            height (int): second argument
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
