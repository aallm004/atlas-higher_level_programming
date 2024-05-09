#!/usr/bin/python3
"""New class called Square is defined"""


class Square:
    """Square is defined"""
    def __init__(self, size=0):
        self.__size = size
        """A private instance attribute: size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Used to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set property of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        print()
        return
