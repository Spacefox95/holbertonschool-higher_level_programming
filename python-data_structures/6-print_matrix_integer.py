#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(' '.join(map(str, row)).format(row))
