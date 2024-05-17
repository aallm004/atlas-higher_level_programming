#!/usr/bin/python3
"""New class that is called BaseGeometry"""


class BaseGeometry:
    """class with public instance method to raise exception"""
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise TypeError("<name> must be greater than 0")
