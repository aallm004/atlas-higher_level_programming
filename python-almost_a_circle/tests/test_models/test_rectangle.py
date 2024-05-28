#!/usr/bin/python3
"""unittests for rectangle.py"""

import os
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Rectangle(unittest.TestCase):
    """test instantiation of the class Rectangle"""

    def test_new_rectangle(self):
        """can a rectangle exist in this universe"""
        Base._Base__nb_object = 0
        r1 = Rectangle(2, 3)
        r2 = Rectangle(2, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_new_rectangle2(self):
        """another form of testulation"""
        self.assertIsNotNone(Rectangle(2, 3))

    def test_new_rectangle3(self):
        """new rectangle"""
        Base._Base__nb_objects = 0  # reset the count
        new = Rectangle(2, 3)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_width_not_a_string1(self):
        """no string with width"""
        with self.assertRaises(TypeError):
            new = Rectangle("2", 2)

    def test_height_not_a_string2(self):
        """no string with height"""
        with self.assertRaises(TypeError):
            new = Rectangle(2, "2")

    def test_x_not_a_string3(self):
        """no string with x"""
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, "2")

    def test_y_not_a_string4(self):
        """no string with y"""
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, 2, "2")

    def test_make_rectangle_with_all_5(self):
        new = Rectangle(2, 20, 200, 2000, 20000)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 20)
        self.assertEqual(new.x, 200)
        self.assertEqual(new.y, 2000)
        self.assertEqual(new.id, 20000)

    def test_width_not_below_0(self):
        """no negativity here"""
        with self.assertRaises(ValueError):
            new = Rectangle(-2, 2)

    def test_height_not_below_0(self):
        """no negativity here"""
        with self.assertRaises(ValueError):
            new = Rectangle(2, -2)

    def test_x_not_below_0(self):
        """no negativity here either"""
        with self.assertRaises(ValueError):
            new = Rectangle(2, 2, -2)

    def test_y_not_below_0(self):
        """be gone with you negativity"""
        with self.assertRaises(ValueError):
            new = Rectangle(2, 2, 2, -2)

    def test_width_not_0(self):
        """no zero here"""
        with self.assertRaises(ValueError):
            new = Rectangle(0, 10)

    def test_height_not_0(self):
        """no zero can live here"""
        with self.assertRaises(ValueError):
            new = Rectangle(10, 0)

    def test_area(self):
        r = Rectangle(20, 20)
        self.assertEqual(r.area(), 200)

    def test_str(self):
        Base._Base__nb_objects = 0
        r = Rectangle(20, 20)
        self.assertEqual(str(r),"[Rectangle] (1) 0/0 - 20/20")

    def test_display_no_x_no_y(self):
        r = Rectangle(20, 3)
        out = "##########\n##########\n"
        with patch('sys.stdout', new=StringIO()) as stdout:
            r.display()
            self.assertEqual(stdout.getvalue(), out)

    def test_display_no_x(self):
        r = Rectangle(20, 3)
        r.y = 3
        out = "\n\n##########\n##########\n"
        with patch('sys.stdout', new=StringIO()) as stdout:
            r.display()
            self.assertEqual(stdout.getvalue(), out)

    def test_display_no_y(self):
        r = Rectangle(20, 3)
        r.x = 3
        out = "  ##########\n  ##########\n"
        with patch('sys.stdout', new=StringIO()) as stdout:
            r.display()
            self.assertEqual(stdout.getvalue(), out)

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0
        r = Rectangle(20, 3)
        d = {'id': 1, 'width': 20, 'height': 3, 'x': 0, 'y': 0} 
        self.assertEqual(r.to_dictionary(), d)

    def test_update_1(self):
        r = Rectangle(20, 200, 2000, 20000, 2)
        r.update()
        self.assertEqual("[Rectangle] (2) 2000/20000 - 20/200", str(r))

    def test_update_2(self):
        r = Rectangle(20, 200, 2000, 20000, 2)
        r.update(3)
        self.assertEqual("[Rectangle] (3) 2000/20000 - 20/200", str(r))

    def test_update_3(self):
        r = Rectangle(20, 200, 2000, 20000, 2)
        r.update(3, 30)
        self.assertEqual("[Rectangle] (3) 2000/20000 - 30/200", str(r))

    def test_update_4(self):
        r = Rectangle(20, 200, 2000, 20000, 2)
        r.update(3, 30, 300)
        self.assertEqual("[Rectangle] (3) 2000/20000 - 30/300", str(r))

    def test_update_5(self):
        r = Rectangle(20, 200, 2000, 20000, 2)
        r.update(3, 30, 300, 3000)
        self.assertEqual("[Rectangle] (3) 3000/20000 - 30/300", str(r))

    def test_update_6(self):
        r = Rectangle(20, 200, 2000, 20000, 2)
        r.update(3, 30, 300, 3000, 30000)
        self.assertEqual("[Rectangle] (3) 3000/30000 - 30/300", str(r))

    def test_create_1(self):
        r = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")

    def test_create_2(self):
        r = Rectangle.create(**{ 'id': 89,
                                 'width': 3 })
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 3/2")

    def test_create_3(self):
        r = Rectangle.create(**{ 'id': 89,
                                 'width': 3,
                                 'height': 3 })
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 3/3")

    def test_create_4(self):
        r = Rectangle.create(**{ 'id': 89,
                                 'width': 3,
                                 'height': 3,
                                 'x': 3 })
        self.assertEqual(str(r), "[Rectangle] (89) 3/0 - 3/3")

    def test_create_5(self):
        r = Rectangle.create(**{ 'id': 89,
                                 'width': 3,
                                 'height': 3,
                                 'x': 3,
                                 'y': 3 })
        self.assertEqual(str(r), "[Rectangle] (89) 3/3 - 3/3")

    def test_save_to_file_none(self):
        r = Rectangle(2,2)
        self.assertEqual(r.save_to_file(None), None)

    def test_save_to_file_emptylist(self):
        r = Rectangle(2,2)
        self.assertEqual(r.save_to_file([]), None)


#Rectangle.create(**{ 'id': 89, 'width': 1 })
#Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
#Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
#Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
#Rectangle.save_to_file(None)
#Rectangle.save_to_file([])
#Rectangle.save_to_file([Rectangle(1, 2)])
#Rectangle.load_from_file() # file doesn't exist
#Rectangle.load_from_file() # file does exist
