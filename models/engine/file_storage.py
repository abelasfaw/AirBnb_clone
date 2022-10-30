#!/usr/bin/python3
"""module to handle file operation of objects"""


import json
from os import path


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects """

        return self.__objects

    def new(self, obj):
        """ adds new instance to __objects"""

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """saves dictionary to json file"""

        with open(self.__file_path, 'w') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """loads objects from json file"""

        if(path.exists(self.__file_path)):
            with open(self.__file_path) as json_file:
                print("inside ", json_file)
                self.__objects = json.load(json_file)
