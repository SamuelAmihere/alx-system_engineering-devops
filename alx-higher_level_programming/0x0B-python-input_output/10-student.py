#!/usr/bin/python3
"""A module with Student class"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Entry point to student object creation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student"""
        return self.__dict__

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
