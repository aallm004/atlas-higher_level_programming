#!/usr/bin/python3
"""define function to return list of available attributes and methods"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
   
   Args:
        obj: object

    Returns:
        list
    """
    
    return dir(obj)
