#!/usr/bin/python3
"""New class called that defines a Rectangle"""


class Rectangle:
    """Nothing takes place, more code to be written"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width
        
        @property
        def height(self):
            return self.__height
        
        @width.setter
        def width(self, value):
            self.__width = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width ust be >= 0")
        
        @height.setter
        def height(self, value):
            self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        
        

        

