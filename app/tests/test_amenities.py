import unittest
import uuid
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from app import create_app

class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        amenity_name = f"Pool-{uuid.uuid4()}"
        response = self.client.post('/api/v1/amenities/', json={"name": amenity_name})
        self.amenity_id = response.get_json().get('id')

    def test_create_amenity(self):
        """Test creating a new amenity with valid data"""
        response = self.client.post('/api/v1/amenities/', json={"name": "Hot Tub"})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertIn('name', data)
        self.assertEqual(data['name'], 'Hot Tub')

    def test_get_amenity(self):
        """Test getting an existing amenity"""
        self.assertIsNotNone(self.amenity_id, "Amenity ID should not be None.")
        response = self.client.get(f'/api/v1/amenities/{self.amenity_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', response.get_json())

    def test_update_amenity(self):
        """Test updating an existing amenity"""
        new_name = "Updated Wifi"
        response = self.client.put(f'/api/v1/amenities/{self.amenity_id}', json={"name": new_name})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], new_name)

    def test_get_nonexist_amenity(self):
        """Test getting a non-existent amenity"""
        response = self.client.get('/api/v1/amenities/888')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Amenity not found', response.get_json()['error'])

    def test_update_nonexistent_amenity(self):
        """Test updating a non-existent amenity"""
        response = self.client.put('/api/v1/amenities/nonexistent-id', json={"name": "Non-Existent"})
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.get_json())

if __name__ == '__main__':
    unittest.main()
