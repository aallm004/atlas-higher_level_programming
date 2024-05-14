#!/usr/bin/python3
"""Class Rectangle which has various attributes"""


class Rectangle:
    """Class Rectangle which defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    """Initialize Rectangle data"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """used to retrieve width"""
        return self._width

    @width.setter
    def width(self, value):
        """used to set width"""
        self._width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = int(value)

    @property
    def height(self):
        """used to retrieve height"""
        return self._height

    @height.setter
    def height(self, value):
        """used to set height"""
        self._height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = int(value)

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        else:
            return 2 * (self._width + self._height)
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2


    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        else:
            string = ""
            for x in range(self._height):
                string += str(self.print_symbol) * self._width
                if x < self._height - 1:
                    string += "\n"
            return string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
