#!/usr/bin/python3

"""
    Module: state

    This module implements the State class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state where cities are located.
    """
    name = ""
