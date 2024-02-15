#!/usr/bin/python3
"""Module with a class Rectangle"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Inherits BaseGeometry from 7-base_geometry.py"""
    def __init__(self, width, height):
        """Instantiates with width and height"""
        self.__width = width
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
