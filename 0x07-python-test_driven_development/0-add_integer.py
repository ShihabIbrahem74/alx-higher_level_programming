#!/usr/bin/python3
"""Add module"""


def add_integer(a, b=98):
    """add two numbers

    Args:
        a (int): first argument
        b (int): second argument, Defaults to 98.

    Raises:
        TypeError: if first argument not int
        TypeError: if second argument not int

    Returns:
        int: sum of two numbers
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError('a must be an integer')
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
