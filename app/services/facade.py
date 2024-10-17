from app.persistence.repository import InMemoryRepository
from app.models.users import User
from app.models.amenities import Amenity
from app.models.places import Place
from app.models.reviews import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.amenities = []  # Keep this for backward compatibility
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
    def create_amenity(self, amenity_data):
        name = amenity_data.get('name')
        if not name:
            raise ValueError("Amenity name is required")

        existing_amenity = self.get_amenity_by_name(name)
        if existing_amenity:
            raise ValueError("Amenity name already exists")

        new_amenity = Amenity(name)
        self.amenity_repo.add(new_amenity)  # Use amenity_repo instead of list
        return new_amenity

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            raise ValueError("Amenity ID doesn't exist")
        return amenity

    def get_amenity_by_name(self, name):
        return self.amenity_repo.get_by_attribute('name', name)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            raise ValueError("Amenity not found")
        self.amenity_repo.update(amenity_id, amenity_data)
        return self.get_amenity(amenity_id)

    # PLACE
    def create_place(self, place_data):
        owner_id = place_data.get('id')  # Changed from 'owner_id' to 'id'
        if not owner_id:
            raise ValueError("id is required")  # Changed error message
        
        owner = self.get_user(owner_id)
        if not owner:
            raise ValueError(f"Owner with id {owner_id} not found")
        
        # Remove id from place_data as we're passing it directly
        place_data.pop('id', None)
        
        place = Place(id=owner_id, **place_data)  # Changed owner to id
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found")
        self.place_repo.update(place_id, place_data)
        return self.get_place(place_id)

    # REVIEW
    def create_review(self, review_data):
        user = self.get_user(review_data['user_id'])
        place = self.get_place(review_data['place_id'])
        if not user or not place:
            raise ValueError("User or Place not found")
        review = Review(user=user, place=place, **review_data)
        self.review_repo.add(review)
        place.add_review(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        if not review:
            raise ValueError("Review not found")
        self.review_repo.update(review_id, review_data)
        return self.get_review(review_id)

    def delete_review(self, review_id):
        review = self.get_review(review_id)
        if not review:
            raise ValueError("Review not found")
        self.review_repo.delete(review_id)
        review.place.reviews.remove(review)