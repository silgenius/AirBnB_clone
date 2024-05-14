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

        return type(self).__objects

    def new(self, obj):
        """
        Adds the given obj to the __objects dictionary with the ke
        <obj class name>.id.
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        type(self).__objects.update({key: obj.to_dict()})

    def save(self):
        """
        Serializes the __objects dictionary to the JSON file specified
        by __file_path.
        """
        try:
            with open(type(self).__file_path, mode="r", encoding="utf-8") as f:
                file_content = f.read()
                if file_content:
                    file_content = json.loads(file_content)
                else:
                    file_content = {}
        except FileNotFoundError:
            file_content = {}

        with open(type(self).__file_path, mode="w", encoding="utf-8") as f:
            for key, value in type(self).__objects.items():
                file_content.update({key: value})
            file_content = json.dumps(file_content)
            f.write(file_content)

    def reload(self):
        """
        Deserializes the JSON file specified by __file_path into the __objects dictionary.
        This operation only occurs if the JSON file exists; otherwise, it does nothing.
        """
        try:
            with open(type(self).__file_path, mode="r", encoding="utf-8") as f:
                type(self).__objects = f.read()
                if type(self).__objects:
                    type(self).__objects = json.loads(type(self).__objects)
        except FileNotFoundError:
            pass
