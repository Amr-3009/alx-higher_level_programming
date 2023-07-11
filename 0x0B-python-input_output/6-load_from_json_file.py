#!/usr/bin/python3
"""function that writes an obj to json"""
import json


def load_from_json_file(filename):
    """write obj to a txt file using json"""

    with open(filename) as f:
        return json.load(f)
