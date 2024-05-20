#!/usr/bin/python3
"""
Function that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(isfile):
    """reads text file and prints to stdout"""
    with open(isfile) as f:
        for line in f:
            print(line, end="")
