#!/usr/bin/python3
"""
A module that defines a Square class inherited from Rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherited from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the class
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    # --------------------------Getters-------------------------
    @property
    def size(self):
        """
        Getter for size
        """
        return self.width

    # --------------------------Setters-------------------------
    @size.setter
    def size(self, value):
        """
        Setter for size
        """
        self.width = value
        self.height = value

    # --------------------------Methods-------------------------
    def __str__(self):
        """
        Returns a string representation of the class
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """
        Updates the class Square
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
