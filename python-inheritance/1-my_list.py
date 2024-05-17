#!/usr/bin/python3
"""New class called MyList that prints a sorted list in ascending order."""
class MyList(list):
    """
    A class "MyList" is initialized
    """
    def print_sorted(self):
        """prints the list sorted in ascending order."""

        print(sorted(self))
