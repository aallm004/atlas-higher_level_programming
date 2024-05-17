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


class Rectangle(BaseGeometry):
    """
    class called Rectangle
    """
    def __init__(self, width, height):
        """
        func __init__
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        """
        func __str__
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        func area
        """
        return self.__width * self.__height
