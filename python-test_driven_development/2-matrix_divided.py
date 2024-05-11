#!/usr/bin/python3
"""2-matrix_divided.py - 2-matrix_divided.py"""


def matrix_divided(matrix, div):
    """
    Function that divides 2 integers or floats made into int

    Args:
        a: first int
        b: second int

    Raises:
        TypeError if is neither int nor float

    Return:
        Result of divided int    
    """
        
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a / b
