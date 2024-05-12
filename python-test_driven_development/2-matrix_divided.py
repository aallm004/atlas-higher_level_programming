#!/usr/bin/python3
"""2-matrix_divided.py - 2-matrix_divided.py"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix

    Args:
        matrix: matrix of ints
        div: number

    Raises:
        TypeError if is neither int nor float
        ZeroDivisionError if an int is 0

    Return:
        Result of divided    
    """
    length = 0
    newMatrix = []

    if len(matrix):
        if not isinstance(div, int) and not isinstance(div, float):
            raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix[0], list):
        raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(matrix[0]) <= 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        newRow = []
        row_len = len(matrix[0])
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if length is 0:
            lenth = len(row)
        elif (len(matrix[row]) != row_len):
            raise TypeError("Each row of the matrix must have the same size")

        for item in row:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError ("matrix must be a matrix (list of lists)"
                                "of integers/floats")
 
            newRow.append(round(item / div, 2))
        newMatrix.append(newRow)
    return newMatrix
