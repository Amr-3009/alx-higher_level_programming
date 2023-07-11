#!/usr/bin/python3
"""Function that convert a str to json"""
import json


def to_json_string(my_obj):
    """Return json repr of a string obj"""

    return json.dumps(my_obj)
