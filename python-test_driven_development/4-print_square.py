#!/usr/bin/python3
"""
print_square = __import__('4-print_square').print_square
create a square variable
import print_square function
"""


def print_square(size):
    """
    print_square: prints a square
    """
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
