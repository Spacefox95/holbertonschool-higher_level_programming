#!/usr/bin/python3
"""
Square : This module defines the Square class
It includes a size attribute
"""


class Square:
    """
    Square : Class that represents a square
    Attributes:
    - size (int): the size of the square.
    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)

    """
    def __init__(self, size=0):
        """
        Initializes a square instance.
        Attributes
        - size (int) : the size of the square. Default is 0
        """
        self.size = size

    @property
    def size(self):
        """
        Getter
        Return size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
            value: set size to value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Initialize a public instance methode.
        Parameters:
        - area : the area of the square
        """
        return (self.__size) ** 2
