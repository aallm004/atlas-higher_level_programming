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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

def update(self, *args, **kwargs):
        """"update a thing"""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
        if kwargs is not None and args is None:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                    self.height = value
                else:
                    setattr(self, key, value)
