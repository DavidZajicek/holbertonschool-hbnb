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
    def text(self, text):
        if isinstance(text, str) and text is not None:
            self._text = text
        else:
            raise ValueError("Text is required and must be a string")

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if 1 <= rating <= 5:
            self._rating = rating
        else:
            raise ValueError("Rating must be between 1 and 5.")

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, place):
        if isinstance(place, Place):  # Ensure place is an instance of Place
            self._place = place
        else:
            raise ValueError("Place must be an instance of Place.")

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        if isinstance(user, User):  # Ensure user is an instance of User
            self._user = user
        else:
            raise ValueError("User must be an instance of User.")
