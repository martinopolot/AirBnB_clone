#!/usr/bin/python3
"""Defines the Amenity Class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity.
    Attribues:
        name (str): The name of the amenity
    """

    name = ""

