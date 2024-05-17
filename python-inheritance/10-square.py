#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""


class Square(__import__("9-rectangle.py").Rectangle):
    """
    class of square
    """
    def __init__(self, size):
        """
        func __init__
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        fucntion __str__
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
