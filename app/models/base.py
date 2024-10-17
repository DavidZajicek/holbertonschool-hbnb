#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self._id = str(uuid.uuid4())  # Use a private variable for id
        self.created_at = datetime.now()  # Timestamp for creation
        self.updated_at = datetime.now()  # Timestamp for updates

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if self._id is None:  # Allow setting only if id is not already set
            self._id = value
        else:
            raise AttributeError("ID is already set and cannot be modified")

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp

