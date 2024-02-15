#!/usr/bin/python3
"""Square class."""


class Square:
    """
    Square class: based on 3-square.py.

    Attributes:
        size: size of square - a side.
    """
    def __init__(self, size=0):
        """Initialize Square class.

        Args:
            size: size of square - a side.
        """
        self.__size = size

    @property
    def size(self):
        """
        Returns the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets size property of the square.

        Args:
            value (int): size of square - a side.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of the square.

        Returns: area of the square
        """
        return self.__size ** 2
