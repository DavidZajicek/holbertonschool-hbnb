#!/usr/bin/python3
from __init__ import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner # User id
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    # def add_review(self, review):
    #     """Add a review to the place."""
    #     self.reviews.append(review)

    # def add_amenity(self, amenity):
    #     """Add an amenity to the place."""
    #     self.amenities.append(amenity)

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, title):
        if len(title) <= 100:
            self.title = title
        else:
            ValueError("title maximum length of 50 characters")

    # description

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        if isinstance(price, float) and price > 0:
            self.price = price
        else:
            ValueError("price must be a positive value")

    @property
    def latitude(self):
        return self.price

    @latitude.setter
    def latitude(self, latitude):
        if isinstance(latitude, float) and -90.0 <= latitude <= 90.0:
            self.latitude = latitude
        else:
            ValueError("latitude must be within the range of -90.0 to 90.0")

    @property
    def longtitude(self):
        return self.price

    @longtitude.setter
    def longtitude(self, longtitude):
        if isinstance(longtitude, float) and -180.0 <= longtitude <= 180.0:
            self.longtitude = longtitude
        else:
            ValueError("longtitude must be within the range of -180.0 to 180.0")

    # owner (User): User instance of who owns the place. This should be validated to ensure the owner exists.

    @property
    def owner(self):
        return self.price

    @owner.setter
    def owner(self, owner):
        # if owner in
