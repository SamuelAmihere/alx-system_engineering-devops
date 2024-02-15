#!/usr/bin/python3
"""A module with append_after(filename="", search_string=""
new_string="")
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file"""
    with open(filename, "r+") as f:
        lines = f.readlines()
        f.seek(0)

        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

        f.truncate()
