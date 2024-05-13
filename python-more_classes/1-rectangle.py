#!/usr/bin/python3
"""New class called that defines a Rectangle"""


class Rectangle:
    """Initialize Rectangle data"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """used to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """used to set width"""
        self._width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = int(value)

    @property
    def height(self):
        """used to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """used to set height"""
        self._height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = int(value)
