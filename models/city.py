#!/usr/bin/python3

"""
    Module: city

    This module implements the City class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a city within a state.
    """
    state_id = ""
    name = ""
