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
        self.__width = value
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if width < 0:
        raise ValueError("width ust be >= 0")

    @property
    def height(self):
        """used to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """used to set height"""
        self.__height = value
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if height < 0:
        raise ValueError("height must be >= 0")
        
        

        

