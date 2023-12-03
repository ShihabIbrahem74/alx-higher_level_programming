#!/usr/bin/python3
"""module for alx task"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str (str)
    """
    dic = json.loads(my_str)
    return (dic)
