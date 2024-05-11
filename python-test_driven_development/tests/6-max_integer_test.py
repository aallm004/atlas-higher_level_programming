#!/usr/bin/python3
'''This module uses unittest to test the module `6-max_integer.py`'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''tests module 6-max_integer.py with multiple function tests'''
    def test_floats(self):
        """Testing a list of floats."""
        floats = [1.23, 4.56, -7.898, 76.5, 43.0]
        self.assertEqual(max_integer(floats), 21.0)

    def test_ints_and_floats(self):
        """Testing a list containing ints and floats."""
        ints_and_floats = [12.3, 4.56, -7, 89, 10]
        self.assertEqual(max_integer(ints_and_floats), 98.7)

    def test_string(self):
        """Testing  for a string."""
        string = "Abigail"
        self.assertEqual(max_integer(string), 'a')

    def test_ordered_list(self):
        """Testing an ordered list of integers."""
        ordered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(max_integer(ordered), 10)

    def test_unordered_list(self):
        """Testing an unordered list of integers."""
        unordered = [2, 4, 6, 3, 1, 8, 10, 9, 5]
        self.assertEqual(max_integer(unordered), 10)

    def test_max_at_begginning(self):
        """Testing a list with a beginning max value."""
        max_at_beginning = [10, 6, 8, 2, 4, 3, 5]
        self.assertEqual(max_integer(max_at_beginning), 10)

    def test_empty_list(self):
        """Testing an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Testing a list with a single element."""
        one_element = [2]
        self.assertEqual(max_integer(one_element), 2)

    def test_list_of_strings(self):
        """Testing a list of strings."""
        strings = ["It", "is", "a", "beautiful" "day"]
        self.assertEqual(max_integer(strings), "day")

    def test_empty_string(self):
        """Testing an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
