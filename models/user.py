#!/usr/bin/python3

"""
    Module: user

    This module implements the User class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user with email, password, first name,
    and last name attributes.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        All attributes defaults to an empty string.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance.
        """
        super().__init__(*args, **kwargs)
