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
