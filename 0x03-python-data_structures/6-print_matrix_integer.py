#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """ function to print a matrix """

    for r in (matrix):
        for c in r:
            end = " " if r.index(c) != len(r) - 1 else ""
            print("{:d}".format(c), end=end)
        print()
