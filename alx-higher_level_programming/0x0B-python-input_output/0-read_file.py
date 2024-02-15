#!/usr/bin/python3
"""A module for read_file function"""


def read_file(filename=""):
    """Reads a file to print its contents"""
    with open(filename, 'r', encoding="UTF-8") as f:
        print(f.read(), end="")
