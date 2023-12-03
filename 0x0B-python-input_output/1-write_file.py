#!/usr/bin/python3
"""module for alx task"""


def write_file(filename="", text=""):
    """rites a string to a text file (UTF8) and returns the number
    of characters written

    Args:
        filename (str): file name. Defaults to "".
        text (str): date to be written. Defaults to "".
    """
    with open(filename, "w") as f:
        return (f.write(text))
