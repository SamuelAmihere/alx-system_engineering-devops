#!/usr/bin/python3
"""A module with write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file """
    n = 0
    with open(filename, 'a', encoding="UTF-8") as f:
        n = f.write(text)
    return (n)
