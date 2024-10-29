#!/usr/bin/python3
import unittest
import uuid
from app import create_app
# from datetime import datetime
# from app.models.user import User
# from app.models.places import Place
# from app.models.reviews import Review

# class TestReviewModel(unittest.TestCase):
#     def setUp(self):
#         """Set up test cases"""
#         self.user = User(
#             first_name="Test",
#             last_name="User",
#             email="test@test.com"
#         )

#         self.place = Place(
#             title="Test Place",
#             description="Test Description",
#             price=100.0,
#             latitude=40.7128,
#             longitude=-74.0060,
#             owner=self.user
#         )

#         self.review = Review(
#             text="Great place!",
#             rating=5,
#             place=self.place,
#             user=self.user
#         )

#     def test_review_attributes(self):
#         """Test if review attributes are set correctly"""
#         self.assertEqual(self.review.text, "Great place!")
#         self.assertEqual(self.review.rating, 5)
#         self.assertEqual(self.review.place, self.place)
#         self.assertEqual(self.review.user, self.user)

#     def test_review_invalid_rating(self):
#         """Test that invalid ratings raise ValueError"""
#         with self.assertRaises(ValueError):
#             Review(
#                 text="Test review",
#                 rating=6,
#                 place=self.place,
#                 user=self.user
#             )

#     def test_review_invalid_text(self):
#         """Test that invalid text raises ValueError"""
#         with self.assertRaises(ValueError):
#             Review(
#                 text=None,
#                 rating=5,
#                 place=self.place,
#                 user=self.user
#             )

#     def test_review_invalid_place(self):
#         """Test that invalid place raises ValueError"""
#         with self.assertRaises(ValueError):
#             Review(
#                 text="Test review",
#                 rating=5,
#                 place="invalid_place",
#                 user=self.user
#             )

#     def test_review_invalid_user(self):
#         """Test that invalid user raises ValueError"""
#         with self.assertRaises(ValueError):
#             Review(
#                 text="Test review",
#                 rating=5,
#                 place=self.place,
#                 user="invalid_user"
#             )

#     def test_review_to_json(self):
#         """Test the toJSON method"""
#         json_data = self.review.toJSON()
#         self.assertEqual(json_data['text'], "Great place!")
#         self.assertEqual(json_data['rating'], 5)
#         self.assertEqual(json_data['user_id'], self.user.id)
#         self.assertEqual(json_data['place_id'], self.place.id)
#         self.assertTrue('created_at' in json_data)
#         self.assertTrue('updated_at' in json_data)

    # Add this new class after the TestReviewModel class
class TestReviewEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_review_api_create(self):
        """Test review creation through API"""
        # Generate a unique email using uuid
        unique_email = f"test_{uuid.uuid4()}@mail.com"
        # Create a test user
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": unique_email
        })
        self.assertEqual(user_response.status_code, 201, f"User creation failed: {user_response.get_json()}")
        user_id = user_response.get_json().get('id')
        self.assertIsNotNone(user_id, "User ID should not be None.")

        # Create a test place
        place_response = self.client.post('/api/v1/places/', json={
            "title": "Test Place",
            "description": "Test Description",
            "price": 100,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": user_id,
            "amenities": []
        })
        self.assertEqual(place_response.status_code, 201, f"Place creation failed: {place_response.get_json()}")
        place_id = place_response.get_json().get('id')
        self.assertIsNotNone(place_id, "Place ID should not be None.")

        # Create a review
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Great place!",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })
        print("Review creation response JSON:", response.get_json())  # Debugging line

        # Check for successful creation
        self.assertEqual(response.status_code, 201)
        self.assertEqual("Great place!", response.get_json()['text'])
        self.assertEqual(5, response.get_json()['rating'])

    # def test_review_api_create(self):
    #     """Test review creation through API"""
    #     # Create a test user
    #     user_response = self.client.post('/api/v1/users/', json={
    #         "first_name": "Jane",
    #         "last_name": "Doe",
    #         "email": "jane.doe@example.com"
    #     })
    #     user_id = user_response.get_json()['id']

    #     # Create a test place
    #     place_response = self.client.post('/api/v1/places/', json={
    #         "title": "Test Place",
    #         "description": "Test Description",
    #         "price": 100,
    #         "latitude": 40.7128,
    #         "longitude": -74.0060,
    #         "owner_id": user_id,
    #         "amenities": []
    #     })
    #     place_id = place_response.get_json()['id']

    #     # Create a review
    #     response = self.client.post('/api/v1/reviews/', json={
    #         "text": "Great place!",
    #         "rating": 5,
    #         "user_id": user_id,
    #         "place_id": place_id
    #     })
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual("Great place!", response.get_json()['text'])
    #     self.assertEqual(5, response.get_json()['rating'])

    def test_review_api_crud_operations(self):
        """Test CRUD operations for reviews through API"""
        # Create test user and place first
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane3.doe@example.com"
        })
        user_id = user_response.get_json()['id']

        place_response = self.client.post('/api/v1/places/', json={
            "title": "Test Place",
            "description": "Test Description",
            "price": 100,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": user_id,
            "amenities": []
        })
        place_id = place_response.get_json()['id']

        # CREATE
        create_response = self.client.post('/api/v1/reviews/', json={
            "text": "Great place!",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })
        self.assertEqual(create_response.status_code, 201)
        review_id = create_response.get_json()['id']

        # READ
        get_response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual("Great place!", get_response.get_json()['text'])

        # UPDATE
        update_response = self.client.put(f'/api/v1/reviews/{review_id}', json={
            "text": "Updated review",
            "rating": 4
        })
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual("Updated review", update_response.get_json()['text'])
        self.assertEqual(4, update_response.get_json()['rating'])

        # DELETE
        delete_response = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertEqual(delete_response.status_code, 200)

        # Verify DELETE
        get_after_delete = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(get_after_delete.status_code, 404)

    def test_get_place_reviews(self):
        """Test getting reviews for a specific place"""
        # Create test user and place first
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane4.doe@example.com"
        })
        user_id = user_response.get_json()['id']

        place_response = self.client.post('/api/v1/places/', json={
            "title": "Test Place",
            "description": "Test Description",
            "price": 100,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": user_id,
            "amenities": []
        })
        place_id = place_response.get_json()['id']

        # Create a review
        self.client.post('/api/v1/reviews/', json={
            "text": "Great place!",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })

        # Get reviews for the place
        response = self.client.get(f'/api/v1/places/{place_id}/reviews')
        self.assertEqual(response.status_code, 200)
        reviews = response.get_json()
        self.assertTrue(isinstance(reviews, list))
        self.assertGreater(len(reviews), 0)

if __name__ == '__main__':
    unittest.main()
