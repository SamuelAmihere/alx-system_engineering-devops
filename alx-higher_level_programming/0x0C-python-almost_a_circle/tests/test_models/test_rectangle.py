#!/usr/bin/python3
"""Module with a unittest class for the Rectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):
    """A class for unittesting the Rectangle class"""
    def setUp(self):
        """Resets the number of objects"""
        Base.__nb_objects = 0

    def test_width(self):
        """
        Test for width
        """
        # assertEquals Test for width
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.width, 8)
        r4 = Rectangle(*[2, 4, 12, 9, 1])
        self.assertEqual(r4.width, 2)

        # assertRaises Test for width
        # TypeError: width must be an integer
        self.assertRaises(TypeError, Rectangle, *["1", 2, 3, 4])
        self.assertRaises(TypeError, Rectangle, *[{0}, 2, 3, 4])
        self.assertRaises(TypeError, Rectangle, *[[1], 2, 3, 4])
        self.assertRaises(TypeError, Rectangle, *[(1,), 2, 3, 4])
        self.assertRaises(TypeError, Rectangle, *[None, 2, 3, 4])
        # ValueError: width must be > 0
        self.assertRaises(ValueError, Rectangle, *[-1, 2, 3, 4])
        self.assertRaises(ValueError, Rectangle, *[0, 2, 3, 4])
        self.assertRaises(ValueError, Rectangle, *[-999999, 2, 3,
                                                   4])

    def test_height(self):
        """
        Test for height
        """
        # assertEquals Test for height
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.height, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.height, 7)
        r4 = Rectangle(2, 4, 12, 9, 1)
        self.assertEqual(r4.height, 4)

        # assertRaises Test for height
        # TypeError: height must be an integer
        self.assertRaises(TypeError, Rectangle, *[1, "2", 3, 4])
        self.assertRaises(TypeError, Rectangle, *[1, {0}, 3, 4])
        self.assertRaises(TypeError, Rectangle, *[1, [2], 3, 4])
        self.assertRaises(TypeError, Rectangle, *[1, (2,), 3, 4])
        self.assertRaises(TypeError, Rectangle, *[1, None, 3, 4])

        # ValueError: height must be > 0
        self.assertRaises(ValueError, Rectangle, *[1, -2, 3, 4])
        self.assertRaises(ValueError, Rectangle, *[1, 0, 3, 4])
        self.assertRaises(ValueError, Rectangle, *[1, -999999, 3, 4])

    def test_x(self):
        """
        Test for x
        """
        # assertEquals Test for x
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.x, r1.x)
        self.assertEqual(r2.x, 0)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.x, 0)
        r4 = Rectangle(2, 4, 12, 9, 1)
        self.assertEqual(r4.x, 12)

        # assertRaises Test for x
        # TypeError: x must be an integer
        self.assertRaises(TypeError, Rectangle, *[1, 2, "3", 4])
        self.assertRaises(TypeError, Rectangle, *[1, 2, {3}, 4])
        self.assertRaises(TypeError, Rectangle, *[1, 2, [3], 4])
        self.assertRaises(TypeError, Rectangle, *[1, 2, (3,), 4])
        self.assertRaises(TypeError, Rectangle, *[1, 2, None, 4])
        # ValueError: x must be >= 0
        self.assertRaises(ValueError, Rectangle, *[1, 2, -3, 4])
        self.assertRaises(ValueError, Rectangle, *[1, 2, -999999, 4])

    def test_y(self):
        """
        Test for y
        """
        # assertEquals Test for y
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 2)
        self.assertEqual(r2.y, r1.y)
        self.assertEqual(r2.y, 0)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.y, 0)
        r4 = Rectangle(2, 4, 12, 9, 1)
        self.assertEqual(r4.y, 9)

        # assertRaises Test for y
        # TypeError: y must be an integer
        self.assertRaises(TypeError, Rectangle, *[1, 2, 3, "4"])
        self.assertRaises(TypeError, Rectangle, *[1, 2, 3, {4}])
        self.assertRaises(TypeError, Rectangle, *[1, 2, 3, [4]])
        self.assertRaises(TypeError, Rectangle, *[1, 2, 3, (4,)])
        self.assertRaises(TypeError, Rectangle, *[1, 2, 3, None])
        # ValueError: y must be >= 0
        self.assertRaises(ValueError, Rectangle, *[1, 2, 3, -4])
        self.assertRaises(ValueError, Rectangle, *[1, 2, 3, -999999])

    def test_all_privates_props(self):
        """
        Test for all properties
        """
        # assertEquals Test for all properties
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 7)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(2, 4, 12, 9, 1)
        self.assertEqual(r4.width, 2)
        self.assertEqual(r4.height, 4)
        self.assertEqual(r4.x, 12)
        self.assertEqual(r4.y, 9)
        self.assertEqual(r4.id, 1)

        # assertRaises Test for all properties
        # TypeError: all parameters
        self.assertRaises(TypeError, Rectangle, *["1", "2"])
        self.assertRaises(TypeError, Rectangle, *[{1}, {2}])
        self.assertRaises(TypeError, Rectangle, *[[1], [2]])
        self.assertRaises(TypeError, Rectangle, *[(1,), (2,)])
        self.assertRaises(TypeError, Rectangle, *[None, None])

        self.assertRaises(TypeError, Rectangle, *["1", "2", 3, 4])
        self.assertRaises(TypeError, Rectangle, *[1, "2", "3", "4"])
        self.assertRaises(TypeError, Rectangle, *["1", "2", "3", "4"])

        self.assertRaises(TypeError, Rectangle, *[{1}, {0}, 3, 4])
        self.assertRaises(TypeError, Rectangle, *[{1}, {0}, {3}, 4])
        self.assertRaises(TypeError, Rectangle, *[{1}, {0}, {3}, {4}])

        self.assertRaises(TypeError, Rectangle, *[1, [2], [3], 4])
        self.assertRaises(TypeError, Rectangle, *[1, [2], [3], [4]])
        self.assertRaises(TypeError, Rectangle, *[[1], [2], [3], [4]])

        self.assertRaises(TypeError, Rectangle, *[1, (2,), (3,), 4])
        self.assertRaises(TypeError, Rectangle, *[(1), 2, (3,), (4,)])
        self.assertRaises(TypeError, Rectangle, *[(1), (2), (3,), (4,)])

        self.assertRaises(TypeError, Rectangle, *[1, None, None, 4])
        self.assertRaises(TypeError, Rectangle, *[1, None, None, None])
        self.assertRaises(TypeError, Rectangle, *[None, None, None, None])

        # ValueError: all parameters
        self.assertRaises(ValueError, Rectangle, *[-1, -2, 3, 4])
        self.assertRaises(ValueError, Rectangle, *[-1, -2, -3, 4])
        self.assertRaises(ValueError, Rectangle, *[-1, -2, -3, -4])

        self.assertRaises(ValueError, Rectangle, *[0, 0, 3, 4])
        self.assertRaises(ValueError, Rectangle, *[0, 0, 0, 4])
        self.assertRaises(ValueError, Rectangle, *[0, 0, 0, 0])

        self.assertRaises(ValueError, Rectangle, *[-999999, -999999, 3, 4])
        self.assertRaises(ValueError, Rectangle, *[-999999, -999999, -999999,
                                                   4])
        self.assertRaises(ValueError, Rectangle, *[-999999, -999999, -999999,
                                                   -999999])

    def test_area(self):
        """
        Test for area
        """
        # assertEquals Test for area
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
        r4 = Rectangle(2, 4, 12, 9, 1)
        self.assertEqual(r4.area(), 8)

        # assertRaises Test for area
        # TypeError: area()
        self.assertRaises(TypeError, r1.area, 1)
        self.assertRaises(TypeError, r2.area, None)
        self.assertRaises(TypeError, r3.area, "1")
        self.assertRaises(TypeError, r4.area, [1])
        self.assertRaises(TypeError, r1.area, (1,))

    def test_display(self):
        """
        Test for display
        """
        # assertEquals Test for display
        r1 = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as fo:
            r1.display()
            self.assertEqual(fo.getvalue(), "##\n##\n")

        r2 = Rectangle(3, 2, 1, 1)
        with patch('sys.stdout', new=StringIO()) as fo:
            r2.display()
            self.assertEqual(fo.getvalue(), "\n ###\n ###\n")

        r2.height = 1
        with patch('sys.stdout', new=StringIO()) as fo:
            r2.display()
            self.assertEqual(fo.getvalue(), "\n ###\n")

        # assertRaises Test for display
        r3 = Rectangle(3, 2)
        self.assertRaises(TypeError, r3.display, 1)
