#!/usr/bin/python3
"""square module"""


class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(item, int) for item in value) or
                not all(item >= 0 for item in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate the area of square

        Returns:
            int: area value
        """
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("".format())
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
