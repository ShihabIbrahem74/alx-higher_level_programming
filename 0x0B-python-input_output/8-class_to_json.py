#!/usr/bin/python3
"""module for alx task"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj: instance of a Class
    """

    return (obj.__dict__)
