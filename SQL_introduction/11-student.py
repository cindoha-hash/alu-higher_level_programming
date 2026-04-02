#!/usr/bin/python3
"""Module that defines a Student class with reload support."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary description of the student."""
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student instance."""
        for key, value in json.items():
            setattr(self, key, value)
