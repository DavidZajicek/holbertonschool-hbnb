#!/usr/bin/python3
from .base import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self._first_name = first_name # maximum length of 50 characters.
        self._last_name = last_name # maximum length of 50 characters.
        self._email = email # Required, must be unique, and should follow standard @email format validation.
        self._is_admin = is_admin  # Defaults to False
        self.reviews = []
        self.places = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if len(value) <= 50:
            self._first_name = value
        else:
            raise ValueError("first_name maximum length of 50 characters")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if len(value) <= 50:
            self._last_name = value
        else:
            raise ValueError("last_name maximum length of 50 characters")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        # regex = [^@]+@[^@]+\.[^@]+
        if '@' in value:
            self._email = value
        else:
            raise ValueError("Email must be unique, and should follow standard email format")

    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        if isinstance(value, bool):
            self._is_admin = value
        else:
            raise ValueError("is_admin must be a boolean value")

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_place(self, place):
        """Add an amenity to the place."""
        self.places.append(place)
