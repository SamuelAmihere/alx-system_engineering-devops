#!/usr/bin/python3
"""Module with a class BaseGeometry"""
import os.path
import json
import csv


class Base:
    """An empty class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    # --------------------------Static Methods-------------------------
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string == "" or json_string is None:
            return []
        return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares"""
        import turtle
        import random

        # Set up the window
        turtle.title("Squares and Rectangles")
        turtle.bgcolor("black")
        turtle.pensize(3)
        turtle.speed(0)
        turtle.hideturtle()

        # Draw the Rectangles and Squares
        # Rectangles are yellow
        for rect in list_rectangles:
            turtle.color("yellow")
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            # Draw the rectangle
            for i in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)

        # Squares are magenta
        for square in list_squares:
            turtle.color("magenta")
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            # Draw the square
            for i in range(2):
                turtle.forward(square.width)
                turtle.right(90)
                turtle.forward(square.height)
                turtle.right(90)
                # print the id in the middle of the square

        turtle.bye()

    # --------------------------Class Methods-------------------------
    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON string representation of list_objs to a file"""

        list_dicts = []

        fd = cls.__name__ + ".json"
        with open(fd, "w") as f:
            if list_objs is None:
                f.write(str(list_dicts))
                return
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
            f.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            new = cls(1)
        elif cls.__name__ == "Rectangle":
            new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file"""
        fd = cls.__name__ + ".json"
        if not os.path.exists(fd):
            return []
        with open(fd, "r") as f:
            list_dicts = cls.from_json_string(f.read())
            list_objs = [cls.create(**dict) for dict in list_dicts]
            return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save the CSV string representation of list_objs to a file"""

        list_dicts = []

        cls_name = cls.__name__
        fd = cls_name + ".csv"
        with open(fd, "w") as f:
            if list_objs is not None:
                if cls_name == "Square":
                    list_dicts = [[ob.id, ob.size, ob.x, ob.y]
                                  for ob in list_objs]
                elif cls_name == "Rectangle":
                    list_dicts = [[ob.id, ob.width, ob.height, ob.x, ob.y]
                                  for ob in list_objs]

            writer = csv.writer(f)
            writer.writerows(list_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from a file"""

        cls_name = cls.__name__
        fd = cls_name + ".csv"

        if not os.path.exists(fd):
            return []

        with open(fd, "r") as f:
            list_dicts = list(csv.reader(f))

        list_objs = []
        if cls_name == "Square":
            for dict in list_dicts:
                dict = [int(i) for i in dict]
                dict = {"id": dict[0], "size": dict[1],
                        "x": dict[2], "y": dict[3]}
                list_objs.append(cls.create(**dict))
        elif cls_name == "Rectangle":
            for dict in list_dicts:
                dict = [int(i) for i in dict]
                dict = {"id": dict[0], "width": dict[1],
                        "height": dict[2], "x": dict[3], "y": dict[4]}
                list_objs.append(cls.create(**dict))

        return list_objs
