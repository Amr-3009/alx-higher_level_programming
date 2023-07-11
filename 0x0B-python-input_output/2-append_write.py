#!/usr/bin/python3
"""Defines a functions which append to a file"""


def append_write(filename="", text=""):
    """Appends a string to the end of file

    Args:
        filename (str): name of file
        text (str): text to append

    Returns:
        characters appended
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
