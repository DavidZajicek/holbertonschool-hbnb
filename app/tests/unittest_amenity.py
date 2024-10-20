import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

# AMENITY UNITTEST

    def test_create_amenity(self):
        """Test creating a new amenity with valid data"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Pool"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Amenity created successfully', response.get_json()['message'])

    def test_create_amenity_invalid_name(self):
        """Test creating a new amenity with invalid data"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid name', response.get_json()['error'])

    def test_get_amenity(self):
        """Test getting a existing amenity"""
        response = self.client.get('/api/v1/amenities/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.get_json()['name'], 'Pool')

    def test_get_nonexist_amenity(self):
        """Test creating a new amenity with invalid data"""
        response = self.client.get('/api/v1/amenities/888')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Amenity does not exist', response.get_json()['error'])

    def test_update_user(self):
        """Test updating the specific amenity"""
        response = self.client.put('/api/v1/amenities/1', json={
            "name": "Wifi Updated"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Amenity updated successfully', response.get_json()['message'])
