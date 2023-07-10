#!/usr/bin/python3
"""
class myList
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Method sorts lists"""

        print(sorted(list(self)))
