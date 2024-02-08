#!/usr/bin/python3
"""
Rectangle : This module defines the Rectangle class
It includes a width and a height attributes
"""


class Rectangle:
    """
    Rectangle : Class that represents a rectangle
    Attributes:
    - width (int): the width of the rectangle.
    Functions:
        __init__(self, width, height)
        width(self)
        height(self)
        width(self, value)
        height(self, value)
        area(self)
        my_print(self)

    """
    def __init__(self, width=0, height=(0, 0)):
        """
        Initializes a rectangle instance.
        Attributes
        - width (int) : the width of the rectangle. Default is 0
        - height (int) : the height of the rectangle. Default is 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Getter
        Return width
        """
        return self.__width

    @property
    def height(self):
        """
        Getter
        Return height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter
        Args:
            value: set width to value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter
        Args:
            value: set height to value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
