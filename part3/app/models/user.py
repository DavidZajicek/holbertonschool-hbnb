""" User model """
import re
from datetime import datetime
from .base import BaseModel
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class User(BaseModel):
    """ User class """
    __tablename__ = 'users'

    _first_name = Column("first_name", String(50), nullable=False)
    _last_name = Column("last_name", String(50), nullable=False)
    _email = Column("email", String(120), nullable=False, unique=True)
    _password = Column("password", String(128), nullable=False)
    _is_admin = Column("is_admin", Boolean, default=False)

    reviews = relationship('Review', back_populates='user', lazy=True)
    places = relationship('Place', back_populates='user', lazy=True)

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        if first_name is None or last_name is None or email is None:
            raise ValueError("Required attributes not specified!")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hash_password(password)
        self.is_admin = is_admin
        self.places = []  # List to store user-owned places
        self.reviews = []  # List to store user-written reviews

    # --- Getters and Setters ---
    # Setters are actually called when values are assigned in the constructor!

    @hybrid_property
    def first_name(self):
        """Getter for prop first_name"""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """Setter for prop first_name"""
        # ensure that the value is up to 50 alphabets only after removing excess white-space
        is_valid_name = 0 < len(value.strip()) <= 50
        if is_valid_name:
            self._first_name = value.strip()
        else:
            raise ValueError("Invalid first_name length!")

    @hybrid_property
    def last_name(self):
        """Getter for prop last_name"""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """Setter for prop last_name"""
        # ensure that the value is up to 50 alphabets only after removing excess white-space
        is_valid_name = 0 < len(value.strip()) <= 50
        if is_valid_name:
            self._last_name = value.strip()
        else:
            raise ValueError("Invalid last_name length!")

    @hybrid_property
    def email(self):
        """Getter for prop email"""
        return self._email

    @email.setter
    def email(self, value):
        """Setter for prop last_name"""
        # calls the method in the facade object
        from app.services import facade

        # add a simple regex check for email format. Nothing too fancy.
        is_valid_email = len(value.strip()) > 0 and re.search(
            "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", value)
        email_exists = facade.get_user_by_email(value.strip())
        if is_valid_email and not email_exists:
            self._email = value
        else:
            if email_exists:
                raise ValueError("Email already exists!")

            raise ValueError("Invalid email format!")

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self._password = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self._password, password)

    @hybrid_property
    def is_admin(self):
        """Getter for prop is_admin"""
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        """Setter for prop is_admin"""
        if isinstance(value, bool):
            self._is_admin = value
        else:
            raise ValueError("Invalid is_admin value!")

    # --- Methods ---

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def add_place(self, place):
        """Add a place to the user."""
        self.places.append(place)

    def add_review(self, review):
        """Add a review to the user."""
        self.reviews.append(review)

    @staticmethod
    def email_exists(email):
        """ Search through all Users to check the email exists """
        # Unused - the facade method get_user_by_email will handle this

    @staticmethod
    def user_exists(user_id):
        """ Search through all Users to ensure the specified user_id exists """
        # Unused - the facade method get_user will handle this
