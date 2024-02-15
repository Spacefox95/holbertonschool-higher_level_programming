#!/usr/bin/python3
"""
Scripts that add all arguments to a Python list
Then, save them to a file
"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_obj = load_from_json_file(filename)
except Exception:
    my_obj = []

save_to_json_file(my_obj + sys.argv[1:], filename)
