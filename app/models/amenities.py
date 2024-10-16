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
    def name(self, value):
        if len(value) <= 50:
            self._name = value
        else:
            raise ValueError("name maximum length of 50 characters")
