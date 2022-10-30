#!/usr/bin/python3
"""Module containing BaseModel to be used by other classes"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class description"""

    def __init__(self, *args, **kwargs):
        """initialize instance"""

        if(len(kwargs) != 0):
            for key, value in kwargs.items():
                if(key == '__class__'):
                    continue
                elif (key == 'created_at' or key == 'updated_at'):
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """string representaion of instance"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.idself.__dict__)

    def save(self):
        """save instance to json file"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """converts instance to to dictionary"""

        result = dict()
        for key, value in self.__dict__.items():
            if(key == 'created_at' or key == 'updated_at'):
                result[key] = value.isoformat()
            else:
                result[key] = value
        result['__class__'] = self.__class__.__name__
        return result
