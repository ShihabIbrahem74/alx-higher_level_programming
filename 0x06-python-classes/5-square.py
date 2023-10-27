#!/usr/bin/python3
"""square module"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """square instance

        Args:
            size (int, optional): value of size. Defaults to 0.

        Raises:
            TypeError: value must be integer
            ValueError: value must be larger than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate the area of square

        Returns:
            int: area value
        """
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("".format())
        for i in range(self.__size):
            for x in range(self.__size):
                print("#".format(), end="")
            print("".format())
