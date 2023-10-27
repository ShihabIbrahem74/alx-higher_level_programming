#!/usr/bin/python3
"""square module"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """square instance

        Args:
            size (int, optional): value of size. Defaults to 0.

        Raises:
            TypeError: must be integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
