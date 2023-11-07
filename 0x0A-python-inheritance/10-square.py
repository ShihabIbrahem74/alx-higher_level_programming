#!/usr/bin/python3
"""module for alx task"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """child class square

    Args:
        Rectangle (parent class): parent class
    """

    def __init__(self, size):
        """init method for square class

        Args:
            size (int): first arguemnt
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
