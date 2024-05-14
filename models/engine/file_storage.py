#!/usr/bin/python3

"""
    Module: file_storage

    This module implements the FileStorage class, which facilitates the
    serialization of instances to a JSON file and deserialization of JSON
    files to instances.
"""

import json


class FileStorage:

    """
    Public instance methods:
    - all(self)
    - new(self, obj)
    - save(self)
    - reload(self)

    Private class attributes:
    - __file_path: string
    - __objects: dictionary
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary containing all stored objects (__objects).
        """

        return self.__objects

    def new(self, obj):
        """
        Adds the given obj to the __objects dictionary with the ke
        <obj class name>.id.
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects.update({key: obj.to_dict()})

    def save(self):
        """
        Serializes the __objects dictionary to the JSON file specified
        by __file_path.
        """
        file_content = {}
        try:
            with open(type(self).__file_path, mode="r", encoding="utf-8") as f:
                file_content = f.read()
                if file_content:
                    file_content = json.loads(file_content)
        except FileNotFoundError:
            pass

        with open(type(self).__file_path, mode="w", encoding="utf-8") as f:
            for key, value in self.__objects.items():
                file_content.update({key: value})
            if file_content:
                file_content = json.dumps(file_content)
                f.write(file_content)

    def reload(self):
        """
        Deserializes the JSON file specified by __file_path into the __objects dictionary.
        This operation only occurs if the JSON file exists; otherwise, it does nothing.
        """
        try:
            with open(type(self).__file_path, mode="r", encoding="utf-8") as f:
                file_content = json.loads(f.read())
                self.__object = {}
                for key, value in file_content.items():
                    cls_name, obj_id = key.split(".")
                    module = __import__("models.base_model", fromlist=[cls_name])
                    cls = getattr(module, cls_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
