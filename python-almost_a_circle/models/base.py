#!/usr/bin/python3
"""Base Class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """json comes to town"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        filename = f"{cls.__name__}.json"

        json_str = cls.to_json_string(list_objs)
        
        list_json = []
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is not None:
                for obj in list_objs:
