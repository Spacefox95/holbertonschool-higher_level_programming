#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            value = matrix[i][j] ** 2
            row.append(value)
        result.append(row)
    return result
