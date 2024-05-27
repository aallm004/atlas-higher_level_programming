#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square Class is created"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this is printing a thing"""
        string = "[Square] (" + str(self.id)
        string += ") " + str(super().x) + "/" + str(super().y)
        string += " - " + str(super().width)
        return string
