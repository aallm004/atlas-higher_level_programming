#!/usr/bin/python3
"""Write a function that returns True if the object is an
instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False. """


def inherits_from(obj, a):
    """returns True if obj is an instance of a subclass
    of given class"""
    if isinstance(obj,a) and type(obj) is not a:
        return True
    else:
        return False
