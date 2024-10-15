#!/usr/bin/python3
from __init__ import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin):
        super().__init__()
        self.first_name = first_name # maximum length of 50 characters.
        self.last_name = last_name # maximum length of 50 characters.
        self.email = email # Required, must be unique, and should follow standard @email format validation.
        self.is_admin = is_admin  # Defaults to False
        self.reviews = []
        self.places = []

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_place(self, place):
        """Add an amenity to the place."""
        self.places.append(place)
