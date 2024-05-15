#!/usr/bin/python3

"""
    Module: user

    This module implements the User class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user with email, password, first name, and last name attributes.

    Attributes:
        email (str): The email of the user. Defaults to an empty string.
        password (str): The password of the user. Defaults to an empty string.
        first_name (str): The first name of the user. Defaults to an empty string.
        last_name (str): The last name of the user. Defaults to an empty string.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
