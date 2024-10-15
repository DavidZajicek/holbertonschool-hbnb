#!/usr/bin/python3
from __init__ import BaseModel
from app.models.__init__ import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place # Place id
        self.user = user # User id
        # relationships many - many

    @property
    def rating(self):
        return self.rating

    @rating.setter
    def rating(self, rating):
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            ValueError("rating must be between 1 and 5.")

# place (Place): Place instance being reviewed. Must be validated to ensure the place exists.
# user (User): User instance of who wrote the review. Must be validated to ensure the user exists
