#!/usr/bin/python3
"""Defines a text file-reading function"""


def read_file(filename=""):
    """Prints contents of texxt file to stdout"""

    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
