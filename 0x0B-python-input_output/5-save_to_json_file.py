#!/usr/bin/python3
"""module for alx task"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj (dict): contains data to convert to json file
        filename (str): json file name
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
