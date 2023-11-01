#!/usr/bin/python3
"""square module"""


def print_square(size):
    """print_square function for alx

    Args:
        size (int): first rgument

    Raises:
        TypeError: if first argument is not int
        ValueError: if size is less than zero
    """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")

    if (size < 0):
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
