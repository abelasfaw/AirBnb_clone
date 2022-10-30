#!/usr/bin/python3
"""Module containing BaseModel to be used by other classes"""


import models
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class description"""

    def __init__(self, *args, **kwargs):
        """initialize instance"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if(len(kwargs) != 0):
            for key, value in kwargs.items():
                if(key == '__class__'):
                    continue
                elif (key == 'created_at' or key == 'updated_at'):
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """string representaion of instance"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """save instance to json file"""

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """converts instance to to dictionary"""

        result = self.__dict__.copy()
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        result['__class__'] = self.__class__.__name__
        return result
