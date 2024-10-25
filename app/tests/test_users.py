import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from app import create_app

class TestUserEndpoints(unittest.TestCase):


    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        # self.client.delete('api/v1/users/1')
        pass

    def test_create_user(self):
        """Test successful user creation"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('jane.doe@example.com', response.get_json()['email'])

    def test_create_user_existing_email(self):
    #create the user first
        self.client.post('/api/v1/users/', json={
            "first_name": "Amy",
            "last_name": "Beford",
            "email": "amy@example.com"
        })
    #test
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "amy@example.com"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Email already registered', response.get_json()['error'])

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Amy",
            "last_name": "Smith",
            "email": "amyemail.com"
            })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Email must follow standard format', response.get_json()['error'])
    
    def test_delete_user(self):
        #create the user first
        create_response = self.client.post('/api/v1/users/', json={
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com"
        })
        self.assertEqual(create_response.status_code, 201)

        user_id = create_response.json['id']
        delete_response = self.client.delete(f'/api/v1/users/{user_id}')
        self.assertEqual(delete_response.status_code, 204)

        get_response = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(get_response.status_code, 404)
        self.assertEqual(get_response.json, {'error': 'User not found'})

    # def test_update_user(self):
    #     Create the user first
    #     user_response = self.client.post('/api/v1/users/', json={
    #         "first_name": "Amy",
    #         "last_name": "Smith",
    #         "email": "amy@example.com"
    #     })

    #     self.assertEqual(user_response.status_code, 201)
    #     self.assertIn('id', user_response.get_json())

    #     user_id = user_response.get_json()['id']

    #     response = self.client.put(f'/api/v1/users/{user_id}', json= {
    #         "first_name": "Amy",
    #         "last_name": "Doe",
    #         "email": "amy.doe@example.com"
    #     })

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.get_json()['first_name'], "Amy")
    #     self.assertEqual(response.get_json()['last_name'], "Doe")
    #     self.assertEqual(response.get_json()['email'], "amy.doe@example.com")

if __name__ == '__main__':
    unittest.main()
