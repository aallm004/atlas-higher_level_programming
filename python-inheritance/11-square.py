#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
"""

class Square(__import__('8-rectangle').Rectangle):
    """
    class Square
    """
    def __init__(self, size):
        """
        func __init__
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(sef):
        """
        func __str__
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
