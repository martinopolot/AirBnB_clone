#!/usr/bin/python3
"""Defines the user class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User.
    Atrributes: 
        email (str): The email of the user.
        password (str): The user pasword.
        first_name (str): The first name of the user
        last_name (str): The last name of the user
    """


    email = ""
    password = ""
    first_name = ""
    last_name = ""
