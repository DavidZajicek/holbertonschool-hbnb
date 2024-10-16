#!/usr/bin/python3
from app.models.base import BaseModel
from app.models.users import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self._title = title
        self._description = description
        self._price = price
        self._latitude = latitude
        self._longitude = longitude
        self._owner = owner  # User id
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if len(value) <= 100:
            self._title = value
        else:
            raise ValueError("Title maximum length of 100 characters")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value is None or isinstance(value, str):
            self._description = value
        else:
            raise ValueError("Description must be a string or None")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, float) and value > 0:
            self._price = value
        else:
            raise ValueError("Price must be a positive value")

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if isinstance(value, float) and -90.0 <= value <= 90.0:
            self._latitude = value
        else:
            raise ValueError(
                "Latitude must be within the range of -90.0 to 90.0")

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if isinstance(value, float) and -180.0 <= value <= 180.0:
            self._longitude = value
        else:
            raise ValueError(
                "Longitude must be within the range of -180.0 to 180.0")

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, User):
            self._owner = value
        else:
            raise ValueError("User must be an instance of User.")

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
