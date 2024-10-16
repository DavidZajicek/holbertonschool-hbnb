from app.persistence.repository import InMemoryRepository
from app.models.places import Place
from app.models.users import User


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    # Places Facade
    def create_place(self, place_data):
        place = Place(
            title=place_data['title'],
            description=place_data['description'],
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner=User('place_holder', 'place_holder', 'placeholder'))
        # owner=self.get_user(place_data['owner_id']))
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        place: Place = self.place_repo.get(place_id)
        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": {
                "id": "place_holder",
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com"
            },
            "amenities": list(place.amenities)
        }

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        pass
