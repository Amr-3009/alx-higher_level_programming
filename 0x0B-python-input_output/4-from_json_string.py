#!/usr/bin/python3
"""function the converts json to obj"""
import json


def from_json_string(my_str):
    """Return str a json str"""

    return json.loads(my_str)
