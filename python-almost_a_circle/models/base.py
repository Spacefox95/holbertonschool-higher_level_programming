#!/usr/bin/python3
"""
Create a new class Base, that will be the base of our geometric forms.
"""
import json


class Base:
    """
    The base class of the project
    Initialize the nb_objects variable
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base class
        Args :
        - id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
