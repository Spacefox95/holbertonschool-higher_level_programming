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
        __init__(self, size, position)
        size(self)
        position(self)
        size(self, value)
        position(self, value)
        area(self)
        my_print(self)

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square instance.
        Attributes
        - size (int) : the size of the square. Default is 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter
        Return size
        """
        return self.__size

    @property
    def position(self):
        """
        Getter
        Return position
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Setter
        Args:
            value: set position to value
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Initialize a public instance methode.
        Parameters:
        - area : the area of the square
        """
        return (self.__size) ** 2

    def my_print(self):
        """
        Print a square in the stdout
        Parameters:
        - size : the size of the square
        - position: the position of the square
        """
        for a in range(self.position[1]):
            print()
        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end='')
            for c in range(self.size):
                print("#", end='')
            print()
        if self.size == 0 or self.position[1] > 0:
            print()
