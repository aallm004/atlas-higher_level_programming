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

        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                A = []
                for o in list_objs:
                    A.append(o.to_dictionary())
                f.write(cls.to_json_string(A))

    def from_json_string(json_string):
        """returning list of JSON string"""
        if json_string is None:
            return []
        return json.loads(json_string)
    
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        obj = cls(1, 1)

        obj.update(**dictionary)

        return obj

