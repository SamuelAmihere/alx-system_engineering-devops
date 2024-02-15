#!/usr/bin/python3
"""Square class."""


class Square:
    """Square class.

    Attributes:
        size (int): size of square - a side.
    """
    def __init__(self, size=0):
        """Initialize Square class.

        Args:
            size: size of square - a side.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
