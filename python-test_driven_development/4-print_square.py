#!/usr/bin/python3
"""
This function prints a square with the character #

Functions:
    def print_square(size)
"""

def print_square(size):
    

    """
    Function that prints a square with the character #

    Args:
        size (int): size of square

    Raises:
        TypeError: if size is not int
        TypeError: if size is less than 0

    Return:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be > 0")

    for i in range(size):
        print("#" * size)
