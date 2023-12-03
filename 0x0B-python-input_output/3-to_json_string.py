#!/usr/bin/python3
"""module for alx task"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)

    Args:
        my_obj (object): will be converted to string
    """
    data = json.dumps(my_obj)
    return (data)
