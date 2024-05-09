#!/usr/bin/python3
"""New class called Square is defined"""


class Square:
    """Square is defined"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Used to retrieve size"""
        return self.__size
    
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        """Setter to set property of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        """Returns current square area"""
        return self.__size ** 2
                                     
    def my_print(self):
        """prints rectangles with # and new line if"""
        if self.__size == 0:
            print()
        else:
            for x in range(self._position[1]):
                print()
            for y in range(self.__size):
                for a in range(self.position[0]):
                    print(" ", end="")
                for b in range(self.size):
                    print("#", end="")
            print()

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(k < 0 for k in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

