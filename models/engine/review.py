#!/usr/bin/python3
"""Defines the review of class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.
    Attributes:
        place_id (str): The Place id.
        user_id ( str): The use id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

