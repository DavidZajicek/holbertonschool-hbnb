from app.persistence.repository import InMemoryRepository
from app.models.amenities import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

# AMENITY
    def __init__(self):
        self.amenities = []

    # def create_amenity(self, amenity_data):
    #     name = amenity_data.get('name')
    #     if not name:
    #         raise ValueError("Amenity name is required")

    #     existing_amenity = self.get_amenity_by_name(name)
    #     if existing_amenity:
    #         raise ValueError("Amenity name alreasy exists")
    #     try:
    #         new_amenity = Amenity(name)  # This will trigger the setter
    #     except ValueError as e:
    #         raise ValueError(str(e))

    #     new_amenity = Amenity(name)
    #     self.amenities.append(new_amenity)
    #     return new_amenity
    def create_amenity(self, amenity_data):
        name = amenity_data.get('name')
        if not name:
            raise ValueError("Amenity name is required")

        existing_amenity = self.get_amenity_by_name(name)
        if existing_amenity:
            raise ValueError("Amenity name already exists")

        # Now this will trigger the name validation
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
