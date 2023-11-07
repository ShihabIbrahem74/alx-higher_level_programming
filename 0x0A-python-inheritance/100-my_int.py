#!/usr/bin/python3
"""module for alx task
"""


class MyInt(int):
    """child class Myint

    Args:
        int (class): parent class
    """

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
