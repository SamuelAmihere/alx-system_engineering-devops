#!/usr/bin/python3
"""A module with Student class"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Entry point to student object creation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
