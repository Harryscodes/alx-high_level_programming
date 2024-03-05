#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    #   return [[col**2 for col in row] for row in matrix]
    new = []
    for row in matrix:
        newrow = []
        for col in row:
            newrow.append(col**2)
        new[len(new):] = [newrow]
    return new
