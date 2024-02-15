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

    def integer_validator(self, name, value):
        """Validates value argument"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
