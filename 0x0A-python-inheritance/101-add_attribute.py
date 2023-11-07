#!/usr/bin/python3
"""module for alx tasks"""


def add_attribute(obj, att, value):
    """alx task method

    Args:
        obj (object): first argument
        att (wtf is this): second argument
        value (int): third argument

    Raises:
        TypeError: can't add new blablbla
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
