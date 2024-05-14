#!/usr/bin/python3
"""
This function prints a line

Functions:
    say_my_name(first_name, last_name): Prints "My name is <first name> <last name>".
"""

def say_my_name(first_name, last_name=""):


    """
    Function that prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name (str): last name

    Raises:
        TypeError: If first_name and last_name are not strings

    Return:
        str: A formatted string with the first name and last name. 
    """

    if not isinstance(first_name, str):
        """Checking to see if the first_name is a string"""
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        """Checking to see if the last_name is a string"""
        raise TypeError("last_name must be a string")

    if last_name:
        print(("My name is {:s} {:s}".format(first_name, last_name)))
        """Printing first_name and last_name"""
    else:
        print(("My name is {:s} ".format(first_name)))
