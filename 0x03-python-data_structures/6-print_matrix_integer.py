#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for coloumns in row:
            print('{:d}'.format(coloumns), end=' ')
        print()
