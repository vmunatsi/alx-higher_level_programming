#!/usr/bin/python3
"""Module 11"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method to_json"""
        return self.__dict__
