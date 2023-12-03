#!/usr/bin/python3
"""module for alx task"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str): file name. Defaults to "".
        text (str): date to be appended. Defaults to "".
    """
    with open(filename, "a") as f:
        return(f.write(text))
