# from app.services.repositories.user_repository import UserRepository
# from app.services.repositories.amenity_repository import AmenityRepository
# from app.services.repositories.place_repository import PlaceRepository
# from app.services.repositories.review_repository import ReviewRepository
# from app.models.user import User
# from app.models.amenity import Amenity
# from app.models.place import Place
# from app.models.review import Review
from app.services.repositories import UserRepository, AmenityRepository, PlaceRepository, ReviewRepository
from app.models import User, Amenity, Place, Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.amenity_repo = AmenityRepository()
        self.place_repo = PlaceRepository()
        self.review_repo = ReviewRepository()

    # In case anyone is curious about the **
    # https://www.geeksforgeeks.org/what-does-the-double-star-operator-mean-in-python/

    # --- Users ---
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        self.user_repo.update(user_id, user_data)

    # --- Amenities ---
    # Used during record insertion to prevent duplicate amenities

    def get_amenity_by_name(self, name):
        return self.amenity_repo.get_by_attribute('name', name)

    def get_amenities_by_place(self, place_id):
        return self.amenity_repo.get_amenities_by_place(place_id)

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        self.amenity_repo.update(amenity_id, amenity_data)

    def create_place_amenity_link(self, place_id, amenity_id):
        return self.amenity_repo.create_place_amenity_link(place_id, amenity_id)

    # --- Places ---

    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_places_by_owner(self, owner_id):
        return self.place_repo.get_places_by_owner(owner_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)

    # --- Reviews ---

    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_reviews_by_place(place_id)

    def get_reviews_by_user(self, user_id):
        return self.review_repo.get_reviews_by_user(user_id)

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)
