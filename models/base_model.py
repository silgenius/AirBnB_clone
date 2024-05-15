#!/usr/bin/python3

"""
    Module: BaseModel

    This module contains the BaseModel class, which serves as a
    foundation for other classes by defining common attributes
    and methods.
"""

import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """
    BaseModel class defines common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        """
        if kwargs and kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "updated_at" or key == "created_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return ("[{}] ({}) {}"
                .format(
                    self.__class__.__name__,
                    self.id,
                    self.__dict__
                    )
                )

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict.update({"__class__": self.__class__.__name__})
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
