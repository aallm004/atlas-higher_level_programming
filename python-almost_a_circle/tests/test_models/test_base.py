import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """test the class Base"""

    def test_id(self):
        """new base can be created?"""
        Base._Base__nb_objects = 0
        base = Base()
        self.assertEqual(base.id, 1)

    def test_make_a_base(self):
        """is the id correct"""
        baseO = Base()
        baseR = Base()
        self.assertEquals(baseO.id, baseR.id - 1)

    def test_assign_id(self):
        """is one able to assign an id"""
        self.assertEqual(98, Base(98).id)

    def test_makes_a_base(self):
        """making new base again?"""
        self.assertIsNotNone(Base())

    def test_to_json_string(self):
        self.assertEquals(Base.to_json_string(None),"[]")

    def test_from_json_string(self):
        self.assertEquals(Base.from_json_string(None), [])
