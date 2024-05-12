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
        first_nam    
    """

    if not isinstance(first_name, str):
        """Checking to see if the first_name is a string"""
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        """Checking to see if the last_name is a string"""
        raise TypeError("last_name must be a string")

    return f"My name is {first_name} {last_name}"

print(("My name is {:s}{:s}".format(first_name, last_name)))
    """Printing first_name and last_name"""
