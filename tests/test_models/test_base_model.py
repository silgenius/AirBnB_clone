import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_str_method(self):
        class_name = self.base_model.__class__.__name__
        expected_str = "[{}] ({}) {}".format(class_name, self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict_method(self):
        class_name = self.base_model.__class__.__name__
        expected_dict = self.base_model.__dict__.copy()
        expected_dict.update({
            'id': self.base_model.id,
            '__class__': class_name,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat()
        })
        self.assertEqual(self.base_model.to_dict(), expected_dict)

class TestBaseModelInit(unittest.TestCase):

    def test_init_with_kwargs(self):
        data = {
            "id": "test_id",
            "created_at": "2024-05-15T12:30:00.000000",
            "updated_at": "2024-05-15T12:30:00.000000",
            "name": "test_name",
            "value": 100
        }
        base_model = BaseModel(**data)
        self.assertEqual(base_model.id, "test_id")
        self.assertEqual(base_model.created_at, datetime.strptime("2024-05-15T12:30:00.000000", "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base_model.updated_at, datetime.strptime("2024-05-15T12:30:00.000000", "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base_model.name, "test_name")
        self.assertEqual(base_model.value, 100)

    def test_init_without_kwargs(self):
        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.id, str))
        self.assertTrue(isinstance(base_model.created_at, datetime))

if __name__ == '__main__':
    unittest.main()

