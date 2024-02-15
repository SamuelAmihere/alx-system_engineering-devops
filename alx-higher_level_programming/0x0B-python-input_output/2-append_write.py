#!/usr/bin/python3
"""A module with append_write function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, 'a', encoding="UTF-8") as f:
        n = f.write(text)
    return (n)
