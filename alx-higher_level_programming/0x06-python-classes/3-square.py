#!/usr/bin/python3
"""Square class."""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """Initialize Square class.

        Args:
            size(int): size of square - a side.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns area of the square."""
        return self.__size ** 2
