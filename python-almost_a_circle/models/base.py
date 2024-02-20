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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(
                [obj.to_dictionary()for obj in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes set
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(width=1, height=1)
            dummy_instance.update(**dictionary)
            return dummy_instance
        else:
            dummy_instance_2 = cls(size=1)
            dummy_instance_2.update(**dictionary)
            return dummy_instance_2

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation
        """
        if json_string is None or json_string == []:
            return []
        else:
            x = json.loads(json_string)
            return x
