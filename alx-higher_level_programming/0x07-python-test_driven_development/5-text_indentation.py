#!/usr/bin/python3
"""
Module has a function that prints 2 new lines after ".?:"
"""


def text_indentation(text):
    """prints 2 new lines after ".?:" characters

    Args:
        text (str): text to print
    Returns:
        Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in ".?:":
        text = text.replace(c, c + "\n\n")
    print("\n".join([line.strip() for line in text.split("\n")]), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
