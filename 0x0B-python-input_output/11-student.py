#!/usr/bin/python3
""" My class module
"""


class Student:
    """ Student class
    """
    def __init__(self, first_name, last_name, age):
        """init

        Args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "[Student] {} - {} - {:d}".format(self.first_name,
                                                 self.last_name, self.age)

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        result_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                result_dict[attr] = getattr(self, attr)
        return result_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
