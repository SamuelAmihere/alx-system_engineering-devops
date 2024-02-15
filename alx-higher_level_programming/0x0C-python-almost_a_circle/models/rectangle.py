#!/usr/bin/python3
"""Module with a class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """A class Rectangle that inherits from Base"""
    __height = 0
    __width = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # ---------------------------Getters-------------------------
    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    # --------------------------Setters-------------------------
    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # --------------------------Methods-------------------------
    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle with the character #"""
        for j in range(self.__y):
            print()
        for h in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle"""
        if args:
            for idx, arg in enumerate(args):
                if idx == 0:
                    self.id = arg
                elif idx == 1:
                    self.__width = arg
                elif idx == 2:
                    self.__height = arg
                elif idx == 3:
                    self.__x = arg
                elif idx == 4:
                    self.__y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Returns a dictionary representation of the rectangle"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
