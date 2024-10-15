#!/usr/bin/python3
from app.models.base import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) <= 50:
            self._name = name
        else:
            ValueError("name maximum length of 50 characters")
