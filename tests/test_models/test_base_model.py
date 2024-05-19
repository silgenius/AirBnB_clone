#!/usr/bin/python3

import unittest
from datetime import datetime
from uuid import UUID
import time
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up for testing"""
        self.model = BaseModel()

    def test_attributes_on_init(self):
        """Test attributes on initialization"""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(UUID(self.model.id), UUID)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_str_representation(self):
        """Test the __str__ method"""
        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected)

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.model.updated_at
        time.sleep(1)  # Sleep for 1 second to ensure the datetime changes
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertGreater(new_updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertNotEqual(model_dict['created_at'], model_dict['updated_at'])

    def test_has_attributes(self):
        """Test if the model has the required attributes"""
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_init_with_kwargs(self):
        """Test initialization with kwargs"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)
        self.assertNotEqual(self.model.created_at, self.model.updated_at)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()

