#!/usr/bin/python3
"""A pyhton module that defines a functions to say names"""


def say_my_name(first_name, last_name=""):
    """prints a name

       Args:
           first_name (str): The first name
           last_name (str): The last name
       Returns:
           Nothing
    """
    for n, name in enumerate([first_name, last_name]):
        if not isinstance(name, str):
            raise TypeError("{} must be a string".format(
                "first_name" if n == 0 else "last_name"))

    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
