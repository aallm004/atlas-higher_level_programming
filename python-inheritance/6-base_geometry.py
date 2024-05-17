#!/usr/bin/python3
"""New class that is called BaseGeometry"""


class BaseGeometry:
    """class with public instance method to raise exception"""
    def area(self):
        raise Exception("area() is not implemented")
