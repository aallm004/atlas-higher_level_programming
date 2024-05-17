#!/usr/bin/python3

"""Function that returns True if the object is an instance of, 
or if the object is an instance of a class that inherited from, 
the specified class ; otherwise False"""

def is_kind_of_class(obj, a):
    """Returns True if object is an instance of the class
        or class that inherited from"""
    return (isinstance(obj, a))
