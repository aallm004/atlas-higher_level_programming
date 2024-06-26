#!/usr/bin/python3
"""Base Class"""
import json
import os


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

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        file_name = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                new_string = my_file.read()
                list_dictionaries = cls.from_json_string(new_string)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances
