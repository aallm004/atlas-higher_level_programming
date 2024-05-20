#!/usr/bin/python3
"""
Function that appends a string
at the end of a text file (UTF8) and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends a string at end of text file
    and returns # of char added"""
    with open(filename, 'a') as f:
        return f.write(text)
