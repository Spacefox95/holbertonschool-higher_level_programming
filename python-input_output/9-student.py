#!/usr/bin/python3
"""
Class Student that defines a student by:
- first_name
- last_name
- age
And retrieves a dictionary representation of a Student instance
"""
class_to_json = __import__('8-class_to_json').class_to_json


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return class_to_json(self)
