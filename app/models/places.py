#!/usr/bin/python3
from base import BaseModel
from app.models.users import User

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self._title = title
        self._description = description
        self._price = price
        self._latitude = latitude
        self._longitude = longitude
        self._owner = owner # User id
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title and len(title) <= 100:
            self._title = title
        else:
            ValueError("title maximum length of 100 characters")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if description is None or isinstance(description, str):
            self._description = description
        else:
            ValueError("Description must be a string or None")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, float) and price > 0:
            self._price = price
        else:
            ValueError("price must be a positive value")

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        if isinstance(latitude, float) and -90.0 <= latitude <= 90.0:
            self._latitude = latitude
        else:
            ValueError("latitude must be within the range of -90.0 to 90.0")

    @property
    def longtitude(self):
        return self._longtitude

    @longtitude.setter
    def longtitude(self, longtitude):
        if isinstance(longtitude, float) and -180.0 <= longtitude <= 180.0:
            self._longtitude = longtitude
        else:
            ValueError("longtitude must be within the range of -180.0 to 180.0")

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if isinstance(owner, User): ### not sure if this is correct
            self._owner = owner
        else:
            raise ValueError("User must be an instance of User.")

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
