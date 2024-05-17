import unittest
from models.user import User
from models.engine.file_storage import FileStorage
import os

class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up for testing"""
        self.user = User()

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_user_attributes(self):
        """Test if User has the correct attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_inheritance(self):
        """Test if User inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_user_serialization(self):
        """Test if User can be serialized and deserialized correctly"""
        storage = FileStorage()
        storage.new(self.user)
        storage.save()
        
        storage.reload()
        user_key = f"User.{self.user.id}"
        self.assertIn(user_key, storage.all())

        deserialized_user = storage.all()[user_key]
        self.assertEqual(deserialized_user.email, "")
        self.assertEqual(deserialized_user.password, "")
        self.assertEqual(deserialized_user.first_name, "")
        self.assertEqual(deserialized_user.last_name, "")

if __name__ == "__main__":
    unittest.main()

