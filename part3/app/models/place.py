from datetime import datetime
from sqlalchemy import Column, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property
from .base import Base, BaseModel
from app.models.user import User


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True)
                      )


class Place(BaseModel):
    __tablename__ = 'places'

    _title = Column('title', String(100), nullable=False)
    _description = Column('description', String(128), nullable=False)
    _price = Column('price', Float, nullable=False)
    _latitude = Column('latitude', Float, nullable=False)
    _longitude = Column('longitude', Float, nullable=False)
    owner_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='places')
    reviews = relationship('Review', back_populates='place', lazy=True)
    amenities = relationship('Amenity', secondary=place_amenity, lazy='subquery',
                             backref=backref('places', lazy=True))

    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        if title is None or description is None or price is None or latitude is None or longitude is None or owner is None:
            raise ValueError("Required attributes not specified!")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # relationship - List to store related reviews
        self.amenities = []  # relationship - List to store related amenities

    # --- Getters and Setters ---
    @hybrid_property
    def title(self):
        """ Returns value of property title """
        return self._title

    @title.setter
    def title(self, value):
        """Setter for prop title"""
        # ensure that the value is up to 100 alphabets only after removing excess white-space
        is_valid_title = 0 < len(value.strip()) <= 100
        if is_valid_title:
            self._title = value.strip()
        else:
            raise ValueError("Invalid title length!")

    @hybrid_property
    def description(self):
        """ Returns value of property description """
        return self._description

    @description.setter
    def description(self, value):
        """Setter for prop description"""
        # Can't think of any special checks to perform here tbh
        self._description = value

    @hybrid_property
    def price(self):
        """ Returns value of property price """
        return self._price

    @price.setter
    def price(self, value):
        """Setter for prop price"""
        if isinstance(value, float) and value > 0.0:
            self._price = value
        else:
            raise ValueError("Invalid value specified for price")

    @hybrid_property
    def latitude(self):
        """ Returns value of property latitude """
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        """Setter for prop latitude"""
        if isinstance(value, float) and -90.0 <= value <= 90.0:
            self._latitude = value
        else:
            raise ValueError("Invalid value specified for Latitude")

    @hybrid_property
    def longitude(self):
        """ Returns value of property longitude """
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        """Setter for prop longitude"""
        if isinstance(value, float) and -180.0 <= value <= 180.0:
            self._longitude = value
        else:
            raise ValueError("Invalid value specified for Longitude")

    @hybrid_property
    def owner(self):
        """ Returns value of property owner """
        return self._owner

    @owner.setter
    def owner(self, value):
        """Setter for prop owner"""
        if isinstance(value, User):
            self.owner_id = value.id
            self._owner = value
        else:
            raise ValueError("Invalid object type passed in for owner!")

    # --- Methods ---
    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    @staticmethod
    def place_exists(place_id):
        """ Search through all Places to ensure the specified place_id exists """
        # Unused - the facade get_place method will handle this
