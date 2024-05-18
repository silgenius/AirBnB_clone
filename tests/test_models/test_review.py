#!/usr/bin/python3

import unittest
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep
import os

class TestReviewParentClass(unittest.TestCase):
    """Test cases for Review class parent that it inherited from BaseModel"""
    
    def test_ReviewParentClass(self):
        self.assertIsInstance(Review(), BaseModel)


class TestReviewInstances(unittest.TestCase):
    """Test for instances of Review class with different cases"""

    def setUp(self):
        self.my_review = Review()

    def test_with_args_and_kwargs(self):
        dtt = datetime.now()
        dtt_iso = dtt.isoformat()
        my_review = Review(
            "18", id="2314564356345",
            created_at=dtt_iso, updated_at=dtt_iso,
            place_id="1", user_id="2", text="Nice place!"
        )
        self.assertEqual(my_review.id, "2314564356345")
        self.assertEqual(my_review.created_at, dtt)
        self.assertEqual(my_review.updated_at, dtt)
        self.assertEqual(my_review.place_id, "1")
        self.assertEqual(my_review.user_id, "2")
        self.assertEqual(my_review.text, "Nice place!")

    def test_with_None_args_kwargs(self):
        my_review = Review(None)
        self.assertNotIn(None, my_review.__dict__.values())


class TestReviewUnique(unittest.TestCase):
    """Test cases for each review attribute in Review class"""

    def setUp(self):
        self.review1 = Review()
        sleep(0.01)
        self.review2 = Review()

    def test_unique_id(self):
        self.assertNotEqual(self.review1.id, self.review2.id)

    def test_unique_timestamps_created_at(self):
        self.assertLess(self.review1.created_at, self.review2.created_at)


class TestReviewAttrTypes(unittest.TestCase):
    """Test cases for types of attributes of Review in Review class"""

    def setUp(self):
        self.my_review = Review()

    def test_Review_id_type(self):
        self.assertIs(type(self.my_review.id), str)

    def test_Review_place_id_type(self):
        self.assertIs(type(self.my_review.place_id), str)

    def test_Review_user_id_type(self):
        self.assertIs(type(self.my_review.user_id), str)

    def test_Review_text_type(self):
        self.assertIs(type(self.my_review.text), str)

    def test_Review_created_at_instance(self):
        self.assertIsInstance(self.my_review.created_at, datetime)
        iso_str = self.my_review.created_at.isoformat()
        self.assertIsInstance(iso_str, str)


class TestReviewMethods(unittest.TestCase):
    """Test cases for different methods on Review instance of Review class"""

    def setUp(self):
        self.my_review = Review()
        
    def test_save_method_changed_value(self):
        pre_updated_at = self.my_review.updated_at
        self.my_review.save()
        self.assertGreater(self.my_review.updated_at, pre_updated_at)


class TestReviewSerialization(unittest.TestCase):
    """Test cases for serialization and deserialization of Review class"""

    def setUp(self):
        """Set up for testing"""
        self.review = Review()

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_review_serialization(self):
        """Test if Review can be serialized and deserialized correctly"""
        storage = FileStorage()
        storage.new(self.review)
        storage.save()
        
        storage.reload()
        review_key = f"Review.{self.review.id}"
        self.assertIn(review_key, storage.all())

        deserialized_review = storage.all()[review_key]
        self.assertEqual(deserialized_review.place_id, "")
        self.assertEqual(deserialized_review.user_id, "")
        self.assertEqual(deserialized_review.text, "")


if __name__ == "__main__":
    unittest.main()

