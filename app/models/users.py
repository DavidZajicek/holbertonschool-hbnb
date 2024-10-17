from app.models.base import BaseModel
import re
import uuid

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False, id=None):
        super().__init__()  # BaseModel will generate and set the id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._is_admin = is_admin

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value and len(value) <= 50:
            self._first_name = value
        else:
            raise ValueError("first_name maximum length of 50 characters")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value and len(value) <= 50:
            self._last_name = value
        else:
            raise ValueError("last_name maximum length of 50 characters")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value and re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
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

    @property
    def id(self):
        return self._id

    def add_review(self, review):
        """Add a review to the user's reviews."""
        self.reviews.append(review)

    def add_place(self, place):
        """Add a place to the user's places."""
        self.places.append(place)
