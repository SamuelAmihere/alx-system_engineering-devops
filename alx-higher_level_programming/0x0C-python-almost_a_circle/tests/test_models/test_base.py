#!/usr/bin/python3
"""Module for unittesting the Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """A class for unittesting the Base class"""
    def setUp(self):
        """Resets the number of objects"""
        Base._Base__nb_objects = 0

    # Test for private class attributes
    # Test for __nb_objects
    def test_id(self):
        """Test for id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)

        b5 = Base(12)
        b6 = Base()
        self.assertEqual(b5.id, 12)
        self.assertEqual(b6.id, 5)

        b7 = Base("3")
        self.assertEqual(b7.id, "3")

    # Test for private class attributes access
    def test_private_class_attributes_access(self):
        """Test for private class attributes access"""
        b = Base()
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    # -------------test for static methods---------------
    # test for to_json_string
    def test_to_json_string(self):
        """Test for to_json_string"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(Base.to_json_string(None), "[]")

        self.assertEqual(Base.to_json_string([{"id": 12}]), '[{"id": 12}]')
        self.assertEqual(Base.to_json_string([{"id": 12}, {"id": 13}]),
                         '[{"id": 12}, {"id": 13}]')

    # test for from_json_string
    def test_from_json_string(self):
        """Test for from_json_string"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}]'),
                         [{"id": 12}])
        self.assertEqual(Base.from_json_string('[{"id": 12}, {"id": 13}]'),
                         [{"id": 12}, {"id": 13}])

    # test for create
    def test_create(self):
        """Test for create"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1 == r2, False)
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 3/5")

        r3 = Rectangle(3, 5, 1, 2, 12)
        r3_dictionary = r3.to_dictionary()
        r4 = Rectangle.create(**r3_dictionary)
        self.assertEqual(r3 == r4, False)
        self.assertEqual(r3 is r4, False)
        self.assertEqual(r3.__str__(), "[Rectangle] (12) 1/2 - 3/5")
        self.assertEqual(r4.__str__(), "[Rectangle] (12) 1/2 - 3/5")

        # test for create square
        s1 = Square(3, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1 == s2, False)
        self.assertEqual(s1 is s2, False)
        self.assertEqual(s1.__str__(), "[Square] (4) 1/0 - 3")
        self.assertEqual(s2.__str__(), "[Square] (4) 1/0 - 3")

    # test for load_from_file
    def test_load_from_file(self):
        """Test for load_from_file"""

        # rectangle
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle(3, 5, 1, 2, 12)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        # assertEqual Test for load_from_file
        self.assertEqual(list_rectangles_input[0].__str__(),
                         list_rectangles_output[0].__str__())
        self.assertEqual(list_rectangles_input[1].__str__(),
                         list_rectangles_output[1].__str__())
        # raise Test for load_from_file
        self.assertRaises(TypeError, Rectangle.load_from_file, *[1, 2, 3])
        self.assertRaises(TypeError, Rectangle.load_from_file, *["1", 2, 3])

        # square
        s1 = Square(3, 1)
        s2 = Square(3, 1, 2, 12)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        # assertEqual Test for load_from_file
        self.assertEqual(list_squares_input[0].__str__(),
                         list_squares_output[0].__str__())
        self.assertEqual(list_squares_input[1].__str__(),
                         list_squares_output[1].__str__())
        # raise Test for load_from_file
        self.assertRaises(TypeError, Square.load_from_file, *[1, 2, 3])
        self.assertRaises(TypeError, Square.load_from_file, *["1", 2, 3])

    # test for save_to_file
    def test_save_to_file(self):
        """Test for save_to_file"""

        # rectangle
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle(3, 5, 1, 2, 12)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        # assertEqual Test for load_from_file
        self.assertEqual(list_rectangles_input[0].__str__(),
                         list_rectangles_output[0].__str__())
        self.assertEqual(list_rectangles_input[1].__str__(),
                         list_rectangles_output[1].__str__())
        self.assertEqual(Rectangle.save_to_file(None), None)
        self.assertEqual(Rectangle.save_to_file([]), None)
        # raise Test for save_to_file
        self.assertRaises(AttributeError, Rectangle.save_to_file, [1, 2])
        self.assertRaises(AttributeError, Rectangle.save_to_file, ["1", 2])
        self.assertRaises(AttributeError, Rectangle.save_to_file, ['r', 'r2'])

        # square
        s1 = Square(3, 1)
        s2 = Square(3, 1, 2, 12)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        # assertEqual Test for load_from_file
        self.assertEqual(list_squares_input[0].__str__(),
                         list_squares_output[0].__str__())
        self.assertEqual(list_squares_input[1].__str__(),
                         list_squares_output[1].__str__())
        self.assertEqual(Square.save_to_file(None), None)
        self.assertEqual(Square.save_to_file([]), None)
        # raise Test for load_from_file
        self.assertRaises(TypeError, Square.load_from_file, *[1, 2, 3])
        self.assertRaises(TypeError, Square.load_from_file, *["1", 2, 3])
        self.assertRaises(TypeError, Square.load_from_file, ['s', 's2'])

    # test for save_to_file_csv
    def test_save_to_file_csv(self):
        """Test for save_to_file_csv"""

        # rectangle
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle(3, 5, 1, 2, 12)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        # assertEqual Test for load_from_file
        self.assertEqual(list_rectangles_input[0].__str__(),
                         list_rectangles_output[0].__str__())
        self.assertEqual(list_rectangles_input[1].__str__(),
                         list_rectangles_output[1].__str__())
        self.assertEqual(Rectangle.save_to_file_csv(None), None)
        self.assertEqual(Rectangle.save_to_file_csv([]), None)
        # raise Test for save_to_file
        self.assertRaises(AttributeError, Rectangle.save_to_file_csv, [1, 2])
        self.assertRaises(AttributeError, Rectangle.save_to_file_csv, ["1", 2])
        self.assertRaises(AttributeError, Rectangle.save_to_file_csv,
                          ['r', 'r2'])

        # square
        s1 = Square(3, 1)
        s2 = Square(3, 1, 2, 12)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        # assertEqual Test for load_from_file
        self.assertEqual(list_squares_input[0].__str__(),
                         list_squares_output[0].__str__())
        self.assertEqual(list_squares_input[1].__str__(),
                         list_squares_output[1].__str__())
        self.assertEqual(Square.save_to_file_csv(None), None)
        self.assertEqual(Square.save_to_file_csv([]), None)
        # raise Test for load_from_file
        self.assertRaises(TypeError, Square.load_from_file_csv, *[1, 2, 3])
        self.assertRaises(TypeError, Square.load_from_file_csv, *["1", 2, 3])
        self.assertRaises(TypeError, Square.load_from_file_csv, ['s', 's2'])

    # test for __str__
    def test_str(self):
        """Test for __str__"""
        # rectangle
        r1 = Rectangle(3, 5, 1)
        # assertEquals Test for __str__
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/0 - 3/5")
        r2 = Rectangle(3, 5, 1, 2, 12)
        self.assertEqual(r2.__str__(), "[Rectangle] (12) 1/2 - 3/5")
        self.assertEqual(type(r2.__str__()), str)
        # assertRaises Test for __str__
        self.assertRaises(TypeError, r1.__str__, *[1, 2, 3])
        self.assertRaises(TypeError, r1.__str__, *["1", 2, 3])

        # square
        s1 = Square(3, 1)
        # assertEquals Test for __str__
        self.assertEqual(s1.__str__(), "[Square] (2) 1/0 - 3")
        s2 = Square(3, 1, 2, 12)
        self.assertEqual(s2.__str__(), "[Square] (12) 1/2 - 3")
        self.assertEqual(type(s2.__str__()), str)
        # assertRaises Test for __str__
        self.assertRaises(TypeError, s1.__str__, *[1, 2, 3])
        self.assertRaises(TypeError, s1.__str__, *["1", 2, 3])
