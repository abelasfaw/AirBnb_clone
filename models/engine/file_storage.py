#!/usr/bin/python3
"""module to handle file operation of objects"""


import json
from os import path


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def getValidClasses(self):
        """return a dictionary of supported classes"""

        from models.base_model import BaseModel
        valid_classes = {"BaseModel": BaseModel}
        return valid_classes

    def all(self):
        """returns __objects """

        return FileStorage.__objects

    def new(self, obj):
        """ adds new instance to __objects"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """saves dictionary to json file"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """loads objects from json file"""

        if(path.exists(self.__file_path)):
            with open(self.__file_path) as json_file:
                loaded_dict = json.load(json_file)
                loaded_dict = {k: self.getValidClasses()[v["__class__"]]
                               (**v) for k, v in loaded_dict.items()}
                FileStorage.__objects = loaded_dict
