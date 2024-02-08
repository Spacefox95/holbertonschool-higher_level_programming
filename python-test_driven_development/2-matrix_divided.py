#!/usr/bin/python3
"""
matrix_divided = __import__('2-matrix_divided').matrix_divided
create a matrix divided variable
import matrix_divider function
"""


def matrix_divided(matrix, div):
    """
    matrix_divided: divides all elements of a matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must\
                         be a matrix (list of lists) of integers/floats")
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    result = [[round(elem / div, 2) for elem in row] for row in matrix]
    return result
