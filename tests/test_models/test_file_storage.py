import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up for testing"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIn(f"BaseModel.{self.model.id}", objects)

    def test_new(self):
        """Test the new method"""
        model2 = BaseModel()
        self.storage.new(model2)
        self.assertIn(f"BaseModel.{model2.id}", self.storage.all())

    def test_save(self):
        """Test the save method"""
        self.storage.save()
        with open("file.json", "r") as file:
            data = json.load(file)
            self.assertIn(f"BaseModel.{self.model.id}", data)

    def test_reload(self):
        """Test the reload method"""
        self.storage.save()
        storage2 = FileStorage()
        storage2.reload()
        self.assertIn(f"BaseModel.{self.model.id}", storage2.all())

    def test_reload_no_file(self):
        """Test the reload method with no file"""
        storage2 = FileStorage()
        try:
            storage2.reload()
        except Exception as e:
            self.fail(f"reload() raised {e.__class__.__name__} unexpectedly!")

if __name__ == "__main__":
    unittest.main()

