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
