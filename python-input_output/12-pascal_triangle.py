#!/usr/bin/python3
"""
Function pascal_triangle:
Returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    my_list = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(my_list[i - 1][j] + my_list[i - 1][j - 1])
        my_list.append(row)
    return my_list
