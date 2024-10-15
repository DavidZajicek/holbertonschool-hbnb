#!/usr/bin/python3
from app.models.base import BaseModel
from app.models.places import Place
from app.models.users import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self._text = text
        self._rating = rating
        self._place = place  # Place instance
        self._user = user    # User instance

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, str) and value is not None:
            self._text = value
        else:
            raise ValueError("Text is required and must be a string")

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if 1 <= value <= 5:
            self._rating = value
        else:
            raise ValueError("Rating must be between 1 and 5")

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        if isinstance(value, Place):  # Ensure place is an instance of Place
            self._place = value
        else:
            raise ValueError("Place must be a valid Place instance.")

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, User):  # Ensure user is an instance of User
            self._user = value
        else:
            raise ValueError("User must be a valid User.")
