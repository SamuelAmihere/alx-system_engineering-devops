#!/usr/bin/python3
"""A module with MyInt class"""


class MyInt(int):
    """Inherits int"""
    def __eq__(self, other):
        """inverts == to !="""
        return int(other) != int(self)

    def __ne__(self, other):
        """inverts != to =="""
        return int(other) == int(self)
