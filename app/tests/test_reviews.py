#!/usr/bin/python3
import unittest
from datetime import datetime
from app.models.user import User
from app.models.places import Place
from app.models.reviews import Review

class TestReviewModel(unittest.TestCase):
    def setUp(self):
        """Set up test cases"""
        self.user = User(
            first_name="Test",
            last_name="User",
            email="test@test.com"
        )
        
        self.place = Place(
            title="Test Place",
            description="Test Description",
            price=100.0,
            latitude=40.7128,
            longitude=-74.0060,
            owner=self.user
        )
        
        self.review = Review(
            text="Great place!",
            rating=5,
            place=self.place,
            user=self.user
        )

    def test_review_attributes(self):
        """Test if review attributes are set correctly"""
        self.assertEqual(self.review.text, "Great place!")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.place, self.place)
        self.assertEqual(self.review.user, self.user)

    def test_review_invalid_rating(self):
        """Test that invalid ratings raise ValueError"""
        with self.assertRaises(ValueError):
            Review(
                text="Test review",
                rating=6,
                place=self.place,
                user=self.user
            )

    def test_review_invalid_text(self):
        """Test that invalid text raises ValueError"""
        with self.assertRaises(ValueError):
            Review(
                text=None,
                rating=5,
                place=self.place,
                user=self.user
            )

    def test_review_invalid_place(self):
        """Test that invalid place raises ValueError"""
        with self.assertRaises(ValueError):
            Review(
                text="Test review",
                rating=5,
                place="invalid_place",
                user=self.user
            )

    def test_review_invalid_user(self):
        """Test that invalid user raises ValueError"""
        with self.assertRaises(ValueError):
            Review(
                text="Test review",
                rating=5,
                place=self.place,
                user="invalid_user"
            )

    def test_review_to_json(self):
        """Test the toJSON method"""
        json_data = self.review.toJSON()
        self.assertEqual(json_data['text'], "Great place!")
        self.assertEqual(json_data['rating'], 5)
        self.assertEqual(json_data['user_id'], self.user.id)
        self.assertEqual(json_data['place_id'], self.place.id)
        self.assertTrue('created_at' in json_data)
        self.assertTrue('updated_at' in json_data)

if __name__ == '__main__':
    unittest.main()