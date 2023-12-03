#!/usr/bin/python3
"""module for alx task"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”

    Args:
        filename (str): file name to be created
    """
    with open(filename, "r") as f:
        new_dict = json.load(f)
        return (new_dict)
