#!/usr/bin/python3
""" numero nueve """


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """__init__ method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        return self.__dict__
