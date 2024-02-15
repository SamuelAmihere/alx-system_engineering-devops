#!/usr/bin/python3
""" A module with a class that inherits from list """


class MyList(list):
    """ Inherits from list
    Parent class: list
    """

    def print_sorted(self):
        """ Prints all elements in ascending order """
        print(sorted(self))
