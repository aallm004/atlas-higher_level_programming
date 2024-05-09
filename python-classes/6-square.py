#!/usr/bin/python3
"""New class called Square is defined"""


class Square:
    """Square is defined"""
    def __init__(self, size=0, position=(0.0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Used to retrieve size"""
        return self.__size
    
    @property
    def position(self):
        return self.__position
    
    def area(self):
        """Returns current square area"""
        return self.__size ** 2

    @size.setter
    def size(self, value):
        """Setter to set property of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def my_print(self):
        """prints rectangles with # and new line if nothing"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.size):
                for x in range(self.position[0]):
                    print(end=" ")
                for a in range(self.__size):
                    print("#", end="")
                print()
