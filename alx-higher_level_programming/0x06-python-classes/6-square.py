#!/usr/bin/python3
"""Square class."""


class Square:
    """
    Square class: based on 3-square.py.

    Attributes:
        size: size of square - a side.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square class.

        Args:
            size: size of square - a side.
            position: position of square - a tuple of 2
                      positive integers.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Returns the size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        Returns the position of the square.
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Sets position property of the square.

        Args:
            value (tuple): position of square - a tuple of 2
                           positive integers.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) \
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates area of the square.

        Returns: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.__size > 0:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        elif self.__size == 0:
            print()
