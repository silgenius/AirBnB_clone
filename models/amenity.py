#!/usr/bin/python3

"""
    Module: amenity

    This module implements the Amenity class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity available in a place.
    """
    name = ""
