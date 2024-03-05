#!/usr/bin/python3

""" module for function to divide matrix """


def matrix_divided(matrix, div):
    """ Check if matrix is a list of lists
    of integers or floats """
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    """ Check if each row of the matrix has the same size """
    row_lengths = {len(row) for row in matrix}
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    """ Check if div is a number (integer or float) """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    """ Check if div is not zero """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform division and round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    
    return new_matrix
