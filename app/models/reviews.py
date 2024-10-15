#!/usr/bin/python3
from app.models.base import BaseModel
from app.models.places import Place
from app.models.users import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place # Place id
        self.user = user # User id
        # relationships many - many

    @property
    def text(self):
        return self.text

    @text.setter
    def text(self, text):
        if isinstance(text, str) and text is not None:
            self.text = text
        else:
            ValueError("Text is required and must be a string")

    @property
    def rating(self):
        return self.rating

    @rating.setter
    def rating(self, rating):
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            ValueError("rating must be between 1 and 5.")

    def place(self):
        return self.place

    @place.setter
    def place(self, place):
        if isinstance(place, Place):
            self.place = place
        else:
            raise ValueError("place must be validated to ensure the place exists")

    @property
    def user(self):
        return self.user

    @user.setter
    def user(self, user):
        if isinstance(user, user):
            self.user = user
        else:
            raise ValueError("user must be validated to ensure the place exists")
