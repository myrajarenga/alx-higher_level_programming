#!/usr/bin/python3

'''
Module with class and init methods
'''
import json


class Base:

    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ intialization """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """return json object"""
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        result = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for i in list_objs:
                result.append(cls.to_dictionary(i))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """Returns deserilizated json string"""
        if json_string:
            return json.loads(json_string)
        else:
            return []
