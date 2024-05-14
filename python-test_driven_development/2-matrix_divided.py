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
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:  # type: ignore
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if all(isinstance(i, list) and len(i) != 0
           for i in matrix) is False:  # type: ignore
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):  # type: ignore
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix_cpy = [row[:] for row in matrix]  # type: ignore
    for i in range(len(matrix_cpy)):
        for j in range(len(matrix_cpy[i])):
            if isinstance(matrix_cpy[i][j], (int, float)) is False:
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
            matrix_cpy[i][j] = round(float(matrix_cpy[i][j]) / div, 2)
    return matrix_cpy
