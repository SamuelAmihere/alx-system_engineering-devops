#!/usr/bin/python3
"""Module with a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits BaseGeometry from 7-base_geometry.py"""
    def __init__(self, width, height):
        """Instantiates with width and height"""
        self.__width = width
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height

    def area(self):
        """Finds area of rectangle
        Returns:
            Area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of rectangle
        Returns:
            String representation of rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
