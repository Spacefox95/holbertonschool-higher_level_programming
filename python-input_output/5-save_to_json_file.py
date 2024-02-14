#!/usr/bin/python3
"""
Function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w', encoding="utf-8") as f:
        x = json.dumps(my_obj)
        f.write(x)
