#!/usr/bin/python3

"""
    Module: review

    This module implements the Review class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review for a place.
    """
    place_id = ""
    user_id = ""
    text = ""
