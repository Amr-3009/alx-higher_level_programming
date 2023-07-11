#!/usr/bin/python3
"""function that writes an obj to json"""
import json


def save_to_json_file(my_obj, filename):
    """write obj to a txt file using json"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)
