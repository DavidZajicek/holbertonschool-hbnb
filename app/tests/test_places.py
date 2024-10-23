import unittest
from app import create_app


class TestPlacesEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_place(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        response = self.client.post('/api/v1/places/', json={
            "title": "string",
            "description": "string",
            "price": 1,
            "latitude": 0,
            "longitude": 0,
            "owner_id": user.get_json()['id'],
            "amenities": [
                "string"
            ]
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('string',
                      response.get_json()['title'])

    def test_create_place_no_user(self):
        response = self.client.post('/api/v1/places/', json={
            "title": "string",
            "description": "string",
            "price": 1,
            "latitude": 0,
            "longitude": 0,
            "owner_id": "invalid_id",
            "amenities": [
                "string"
            ]
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid input data', response.get_json()['error'])
