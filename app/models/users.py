#!/usr/bin/python3
from base import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
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

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if len(first_name) <= 50:
            self.first_name = first_name
        else:
            raise ValueError("first_name maximum length of 50 characters")

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, last_name):
        if len(last_name) <= 50:
            self.last_name = last_name
        else:
            raise ValueError("last_name maximum length of 50 characters")

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        # regex = [^@]+@[^@]+\.[^@]+
        if '@' in email:
            self.email = email
        else:
            raise ValueError("email must be unique, and should follow standard email format")

    @property
    def is_admin(self):
        return self.is_admin

    @is_admin.setter
    def is_admin(self, value):
        if isinstance(value, bool):
            self.is_admin = value
        else:
            raise ValueError("is_admin must be a boolean value")
