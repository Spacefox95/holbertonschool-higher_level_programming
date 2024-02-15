#!/usr/bin/python3
"""
 Function that returns the dictionary description with simple data structure :
  - list
  - dictionary
  - string
  - integer
  - boolean
 for JSON serialization of an object
"""
import json


def class_to_json(obj):
    return json.dumps(obj, default=lambda o: o.__dict__)
