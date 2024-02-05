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

    """
    def __init__(self, size=0):
        """
        Initializes a square instance.
        Parameterd:
        - size (int) : the size of the square. Default is 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Initialize a public instance methode.
        Parameters:
        - area : the area of the square
        """
        area = self.__size ** 2
        return area
