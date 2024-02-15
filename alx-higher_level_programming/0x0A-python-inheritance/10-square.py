#!/usr/bin/python3
"""Module with a Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle from 9-rectangle.py"""
    def __init__(self, size):
        """Instantiates with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Finds area of Square
        Returns:
            Area of Square
        """
        return self.__size ** 2
