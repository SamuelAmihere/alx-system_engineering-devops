#!/usr/bin/python3
"""Module with a class BaseGeometry"""


class BaseGeometry:
    """ has a public instance method:
    def area(self): raises an
    Exception with the message area() is not implemented
    """
    def area(self):
        """raises Exception"""
        raise Exception("area() is not implemented")
