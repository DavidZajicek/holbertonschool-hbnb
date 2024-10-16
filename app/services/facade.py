from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

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

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass
