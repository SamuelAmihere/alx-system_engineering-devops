#!/usr/bin/python3
"""A pyhton module that defines Rectangle class"""


class Rectangle:
    """A rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle class.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Returns height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets width property of the rectangle.

        Args:
            value (int): width value.

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets size property of the rectangle.

        Args:
            value (int): height value.

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates area of the rectangle.

        Returns: area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates perimeter of the rectangle.

        Returns: perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """
        Determines string representation of the rectangle with character #.

        Returns: string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(self.__height * ["#" * self.__width])

    def __repr__(self):
        """
        Determines string representation of the rectangle.

        Returns: string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
