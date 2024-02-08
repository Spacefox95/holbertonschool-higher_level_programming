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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance.
        Attributes
        - width (int) : the width of the rectangle. Default is 0
        - height (int) : the height of the rectangle. Default is 0
        - number_of_instances : count the number of instances
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        self.number_of_instances = Rectangle.number_of_instances

    def __str__(self):
        """
        Initialize an instance of str representation of the rectangle
        Return "#" for the width and the height
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width
                          for _ in range(self.height)])

    def __repr__(self):
        """
        Initialize an instance of representation of object Rectangle
        Return the object with his attributes
        """
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """
        Initialize a message when instance Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
