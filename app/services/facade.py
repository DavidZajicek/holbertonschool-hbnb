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
        print(f"User created: {user.id}")
        print(f"All users after creation: {self.user_repo.get_all()}")
        return user

    def get_user(self, user_id):
        """Fetch an User by their ID"""
        user = self.user_repo.get(user_id)
        print(f"Attempting to get user with id: {user_id}")
        print(f"User retrieved: {user}")
        print(f"All users in repository: {self.user_repo.get_all()}")
        return user

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
        owner_id = place_data.get('owner_id')
        if not owner_id:
            raise ValueError("owner_id is required")
        
        print(f"Attempting to retrieve owner with id: {owner_id}")
        owner = self.get_user(owner_id)
        print(f"Retrieved owner: {owner}")
        
        if not owner:
            all_users = self.user_repo.get_all()
            print(f"All users in repository: {all_users}")
            raise ValueError(f"Owner with id {owner_id} not found")
        
        place_data.pop('owner_id', None)
        
        place = Place(owner=owner, **place_data)
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
        user = self.user_repo.get(review_data['user_id'])
        place = self.place_repo.get(review_data['place_id'])
        if not user or not place:
            raise ValueError("Invalid user_id or place_id")
        if not 1 <= review_data['rating'] <= 5:
            raise ValueError("Rating must be between 1 and 5")
        review = Review(review_data['text'], review_data['rating'], place, user)
        self.review_repo.add(review)
        print(f"Review created: {review}, place: {review.place}, user: {review.user}")
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")
        return [review for review in self.review_repo.get_all() if review.place.id == place_id]

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        if 'rating' in review_data and not 1 <= review_data['rating'] <= 5:
            raise ValueError("Rating must be between 1 and 5")
        review.update(review_data)
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        self.review_repo.delete(review_id)

    def get_place_reviews(self, place_id):
        """Get all reviews for a specific place"""
        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found")
    
        all_reviews = self.review_repo.get_all()
        place_reviews = []
    
        for review in all_reviews:
            if hasattr(review, 'place') and hasattr(review.place, 'id'):
                if review.place.id == place_id:
                    place_reviews.append(review)
            else:
                print(f"Warning: Invalid review object found: {review}")
    
        return place_reviews