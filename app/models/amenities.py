#!/usr/bin/python3
from __init__ import BaseModel
from app.models.__init__ import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if len(name) <= 50:
            self.name = name
        else:
            ValueError("name maximum length of 50 characters")
