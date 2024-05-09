#!/usr/bin/python3
"""New class called Square is defined"""


class Square:
    """Square is defined"""
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Used to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set property of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value)!= 2 or not all(isinstance(i, int) and i > 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns current square area"""
        return self.__size ** 2
                                     
    def my_print(self):
        """prints rectangles with # and new line if"""
        if self.__size == 0:
            print()
            return
        for x in range(self._position[1]):
            print()
        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            print("#" * self.__size)
