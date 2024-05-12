#!/usr/bin/python3
def say_my_name(first_name, last_name=""):


    """
    Function that prints My name is <first name> <last name>

    Args:
        first_name: first name
        last_name: last name

    Raises:
        TypeError if first_name and last_name are not strings

    Return:
        first_name and last_name    
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(("My name is {:s}{:s}".format(first_name, last_name)))
