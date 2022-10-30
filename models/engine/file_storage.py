#!/usr/bin/python3
import json
from os import path
class FileStorage:
    __file_path="file.json"
    __objects={}
    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        with open(self.__file_path, 'w') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        if(path.exists(self.__file_path)):
            with open(self.__file_path) as json_file:
                print("inside ", json_file)
                self.__objects = json.load(json_file)
    
