#!/usr/bin/python3
"""Defines a python class to json function"""


def class_to_json(obj):
    """Return dict repr of a simple data struct"""

    return obj.__dict__
