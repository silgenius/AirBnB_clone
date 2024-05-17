import unittest
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class TestState(unittest.TestCase):

    def setUp(self):
        """Set up for testing"""
        self.state = State()

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_state_attributes(self):
        """Test if State has the correct attributes"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_state_inheritance(self):
        """Test if State inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_state_serialization(self):
        """Test if State can be serialized and deserialized correctly"""
        storage = FileStorage()
        storage.new(self.state)
        storage.save()
        
        storage.reload()
        state_key = f"State.{self.state.id}"
        self.assertIn(state_key, storage.all())

        deserialized_state = storage.all()[state_key]
        self.assertEqual(deserialized_state.name, "")

if __name__ == "__main__":
    unittest.main()

