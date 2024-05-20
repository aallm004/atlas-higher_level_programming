#!/usr/bin/python3
"""
Write a function that writes a string to a text file (UTF8) and
returns the number of characters written

"""


def write_file(filename="", text=""):
    """writes string to a text file and returns number of chars"""
    with open(filename, 'w') as f:
        return f.write(text)
