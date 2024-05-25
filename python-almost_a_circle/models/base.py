#!/usr/bin/python3
"""Base Class"""


class Base:
    """Base Class is created"""

    id = 0
    __nb_objects = 0

    def __init__(self, id=None):
        """incrementation of nb"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
