#!/usr/bin/python3
"""
documentation
"""


def class_to_json(obj):
    """
    function that returns the dictionary description
    with simple data structure (list, dict, string, int, boolean)
    for JSON serialization of an object

    Args:
        obj: Object to be serialized

    Returns:
        dict: dictionary representation of the object
    """
    return obj.__dict__
