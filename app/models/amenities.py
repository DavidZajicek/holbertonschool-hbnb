#!/usr/bin/python3
from __init__ import BaseModel
from app.models.__init__ import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
