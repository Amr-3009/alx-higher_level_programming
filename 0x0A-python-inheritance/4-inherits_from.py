#!/usr/bin/python3
"""
4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    returns true if an object is an instance of a class
    """

    return False if type(obj) is a_class else isinstance(obj, a_class)
