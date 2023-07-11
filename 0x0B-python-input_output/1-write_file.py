#!/usr/bin/python3
"""Defines a function that overwrites/creates files"""


def write_file(filename="", text=""):
    """write a string(text) to a file

    Args:
        filename (str): name of the file to write
        text (str): the text to write in the file

    Returns:
        the number of characters written
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
