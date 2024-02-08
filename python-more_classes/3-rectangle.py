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
        perimeter(self)

    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance.
        Attributes
        - width (int) : the width of the rectangle. Default is 0
        - height (int) : the height of the rectangle. Default is 0
        """
        self.height = height
        self.width = width

    def __str__(self):
        """
        Initialize an instance of str representation of the rectangle
        Return "#" for the width and the height
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

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

    def area(self):
        """
        Initialize a method to return rectangle's area
        - area: the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Initialize a method to return rectangle's perimeter
        - perimeter: the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
