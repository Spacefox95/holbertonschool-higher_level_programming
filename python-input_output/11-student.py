#!/usr/bin/python3
"""
Class Student that defines a student by:
- first_name
- last_name
- age
And retrieves a dictionary representation of a Student instance
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if isinstance(i, str) and hasattr(self, i):
                    new_dict[i] = getattr(self, i)
            return new_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
