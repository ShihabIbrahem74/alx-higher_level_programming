#!/usr/bin/python3
"""module for alx task"""


def is_same_class(obj, a_class):
    """is_same_class method

    Args:
        obj (object): return all directories
        a_class (object): class of object
    """
    if type(obj) == a_class:
        return True
    else:
        return False
