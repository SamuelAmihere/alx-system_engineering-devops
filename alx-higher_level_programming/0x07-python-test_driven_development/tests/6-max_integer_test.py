#!/usr/bin/python3
"""A pyhton module for unittesting the max_integer function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class MaximumInt(unittest.TestCase):
    """A class for unittesting the max_integer function"""
    def test_max(self):
        """Test for max_integer function"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9]), 9)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 9, 8]), 9)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 9, 8, 7]), 9)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 9, 8, 7, 6]), 9)
        self.assertEqual(max_integer([1, 2, 3, 4, 9, 8, 7, 6, 5]), 9)
        self.assertEqual(max_integer([1, 2, 3, 9, 8, 7, 6, 5, 4]), 9)
        self.assertEqual(max_integer([1, 2, 9, 8, 7, 6, 5, 4, 3]), 9)
        self.assertEqual(max_integer([1, 9, 8, 7, 6, 5, 4, 3, 2]), 9)
        self.assertEqual(max_integer([9, 8, 7, 6, 5, 4, 3, 2, 1]), 9)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([-1, -5, -3, -2, -4]), -1)
        self.assertEqual(max_integer([7, 4, 9, 2, 1, 5]), 9)
        self.assertEqual(max_integer([6, 8, 3, 1, 2, 7]), 8)
        self.assertEqual(max_integer([1, 3, 5, 7, 9]), 9)
        self.assertEqual(max_integer([2, 4, 6, 8]), 8)
        self.assertEqual(max_integer([1, 2, True, 4]), 4)
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([-1, -3, -2]), -1)

    def test_dtype(self):
        """test for datatype"""
        self.assertRaises(TypeError, max_integer, [1, 2, 3j, 4])
        self.assertRaises(TypeError, max_integer, [1, 2, {3}, 4])
        self.assertRaises(TypeError, max_integer, [1, 2, "3", 4])
        self.assertRaises(TypeError, max_integer, [1, 2, "Sam"])
        self.assertRaises(TypeError, max_integer, [1, 2, None, 4])
        self.assertRaises(TypeError, max_integer, [1, 2, (3,), 4])
        self.assertRaises(TypeError, max_integer, [1, 2, [3], 4])

    def test_empty(self):
        """test for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_none(self):
        """test for none"""
        self.assertRaises(TypeError, max_integer, None)
