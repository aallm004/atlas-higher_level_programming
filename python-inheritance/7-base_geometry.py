#!/usr/bin/python3
"""New class that is called BaseGeometry"""


class BaseGeometry:
    """class with public instance method to raise exception"""
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
