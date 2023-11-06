#!/usr/bin/python3
"""module for alx task"""


def inherits_from(obj, a_class):
    """method for alx task

    Args:
        obj (object): first argument
        a_class (class): second argumement
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
