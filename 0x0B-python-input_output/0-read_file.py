#!/usr/bin/python3
"""module for alx task"""


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout:

    Args:
        filename (str): file name. Defaults to "".
    """
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
