#!/usr/bin/python3

def get_class(str_class):
    module_name = {"BaseModel": "base_model", "User": "user", "Place": "place",
                            "State": "state", "City": "city", "Amenity": "amenity",
                            "Review": "review"}
    module = __import__("models." + module_name[str_class], fromlist=[cls_name])
    cls = getattr(module, str_class)
    return cls
