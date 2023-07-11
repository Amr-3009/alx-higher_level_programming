#!/usr/bin/python3
"""defines a student class"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a dict repr"""
        return self.__dict__
