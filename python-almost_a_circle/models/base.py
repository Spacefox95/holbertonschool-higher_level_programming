#!/usr/bin/python3
"""
Create a new class Base, that will be the base of our geometric forms.
"""


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
