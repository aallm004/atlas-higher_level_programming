#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Base Class Rectagle is created"""
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """Initialize Rectangle data"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """used to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter to set property of width"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """used to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to set property of height"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """used to retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter to set property of x"""
        self.__x = value
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """used to retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter to set property of y"""
        self.__y = value
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """print rectangle"""
        for y in range(0, self.__y):
            print()
        for h in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for w in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        string = "[Rectangle] (" + str(self.id)
        string += ") " + str(self.__x) + "/" + str(self.__y)
        string += " - " + str(self.__width) + "/" + str(self.__height)
        return string

    def update(self, *args):
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass
