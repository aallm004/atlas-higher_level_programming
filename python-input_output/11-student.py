#!/usr/bin/python3
""" numero diez """


class Student:
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        """__init__ method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_space = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    new_space[k] = v
            return new_space

    def reload_from_json(self, json):
        for k, v in json.items()
            setattr(self, k v)
