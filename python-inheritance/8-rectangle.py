#!/usr/bin/python3
"""
write a class Rectange that inherits from BaseGeometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class called Rectangle
    """
    def __init__(self, width, height):
        """
        function __init__
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
