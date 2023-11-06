#!/usr/bin/python3
"""module for alx task"""


def is_kind_of_class(obj, a_class):
    """method for alx task

    Args:
        obj (object): first argument
        a_class (class): second argumement
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
