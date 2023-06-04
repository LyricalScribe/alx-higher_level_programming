#!/usr/bin/python3

""""instantiates a class and converts its items
to json representation"""


class Student:
    """Defines a student class with a method to
    represent it in JSON"""

    def __init__(self, first_name, last_name, age):
        """Instantiates the class object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts class attributes to JSON
        representation"""
        if isinstance(attrs, list) and\
                all(isinstance(item, str) for item in attrs):
            result = {}
            for i in attrs:
                try:
                    result[i] = self.__dict__[i]
                except Exception:
                    pass
            return result
        elif attrs is None:
            return self.__dict__

    def reload_from_json(self, json):
        """Deserialization process"""

        for i in json.keys():
            self.__dict__[i] = json[i]
        return self.__dict__
