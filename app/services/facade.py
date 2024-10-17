from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenities import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
# USER
    def create_user(self, user_data):
        """Creates a new user and saves it to the repository"""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Fetch an User by their ID"""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Fetch a user by their email address"""
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        """Fetch all users"""
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        """Update an existing user"""
        user = self.user_repo.get(user_id)
        if not user:
            return None

        self.user_repo.update(user_id, user_data)
        updated_user = self.user_repo.get(user_id)
        return updated_user

# AMENITY
    def __init__(self):
        self.amenities = []

    def create_amenity(self, amenity_data):
        name = amenity_data.get('name')
        if not name:
            raise ValueError("Amenity name is required")

        existing_amenity = self.get_amenity_by_name(name)
        if existing_amenity:
            raise ValueError("Amenity name already exists")

        new_amenity = Amenity(name)
        self.amenities.append(new_amenity)
        return new_amenity

    def get_amenity(self, amenity_id):
        for amenity in self.amenities:
            if amenity.id == amenity_id:
                return amenity
        raise ValueError("Amenity ID doesn't exist")

    def get_amenity_by_name(self, name):
        for amenity in self.amenities:
            if amenity.name == name:
                return amenity
        return None

    def get_all_amenities(self):
        return self.amenities

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            raise ValueError("ID is not found")

        if 'name' in amenity_data:
            name = amenity_data['name']
            amenity.name = name
        print("Amenity updated successfully")
        return amenity
