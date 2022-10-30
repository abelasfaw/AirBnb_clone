#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
class BaseModel:
    def __init__(self, *args, **kwargs):
        if(len(kwargs) != 0):
            for key, value in kwargs.items():
                if(key == '__class__'):
                    continue
                elif (key == 'created_at' or key == 'updated_at'):
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        result = dict()
        for key, value in self.__dict__.items():
            if(key == 'created_at' or key == 'updated_at'):
                result[key] = value.isoformat()
            else:
                result[key] = value
        result['__class__'] = self.__class__.__name__
        return result

