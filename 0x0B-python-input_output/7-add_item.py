#!/usr/bin/python3
"""module for alx task"""
import json
import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

data = []
file_name = "add_item.json"
if os.path.exists(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)
if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        data.append(i)

with open(file_name, "w") as f:
    json.dump(data, f)
