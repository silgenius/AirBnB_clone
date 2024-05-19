#!/usr/bin/python3

import unittest
from models.user import User
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
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

class TestUserParentClass(unittest.TestCase):
    """test cases for user class parent that inherited from """

    def test_parentClass(self):
        self.assertIsInstance(User(), BaseModel)

class TestUserInstances(unittest.TestCase):
    """test for instances of user class setup 2 users then test them in different cases"""

    def setUp(self):
        self.user1 = User()
        self.user2 = User()

    def test_with_args_and_kwargs(self):
        dtt = datetime.now()
        dtt_iso = dtt.isoformat()
        my_user = User(
            "22", id="1423456667286",
            created_at=dtt_iso, updated_at=dtt_iso,
            email="ray@yahoo.com", password="ray223$",
            first_name="Ray", last_name="Edward"
        )
        self.assertEqual(my_user.id, "1423456667286")
        self.assertEqual(my_user.created_at, dtt)
        self.assertEqual(my_user.updated_at, dtt)
        self.assertEqual(my_user.email, "ray@yahoo.com")
        self.assertEqual(my_user.password, "ray223$")
        self.assertEqual(my_user.first_name, "Ray")
        self.assertEqual(my_user.last_name, "Edward")

    def test_with_None_args_kwargs(self):
        my_user = User(None)

        self.assertNotIn(None, my_user.__dict__.values())



class TestUserUniqueness(unittest.TestCase):
    """Test cases for uniqueness of each user attributes in user class"""

    def setUp(self):
        self.user1 = User()
        sleep(0.02)
        self.user2 = User()

    def test_unique_id(self):
        self.assertNotEqual(self.user1.id, self.user2.id)


    def test_unique_timestamps_created_at(self):
        self.assertNotEqual(
            self.user2.created_at, self.user1.created_at
            )


class TestUserAttrTypes(unittest.TestCase):
    """Test cases for types of attributes of user in user class"""
    def setUp(self):
        self.my_user = User()

    def test_User_id_type(self):
        self.assertIs(type(self.my_user.id), str)

    def test_User_first_name_type(self):
        self.assertIs(type(self.my_user.first_name), str)

    def test_User_last_name_type(self):
        self.assertIs(type(self.my_user.last_name), str)

    def test_User_email_type(self):
        self.assertIs(type(self.my_user.email), str)

    def test_User_password_type(self):
        self.assertIs(type(self.my_user.password), str)

    def test_User_created_at_instance(self):
        self.assertIsInstance(self.my_user.created_at, datetime)
        iso_str = self.my_user.created_at.isoformat()
        self.assertIsInstance(iso_str, str)

class TestUserMethods(unittest.TestCase):
    """test cases for different methods on user instance of user class"""

    def setUp(self):
        self.user = User()

    def test_save_method_changed_value(self):
        pre_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, pre_updated_at)
        self.assertGreater(self.user.updated_at, pre_updated_at)

    def test_save_method_Unintentional_change(self):
        pre_name = self.user.first_name
        pre_email = self.user.email
        updated_name = "Martin"
        self.user.first_name = updated_name
        self.user.save()
        self.assertNotEqual(self.user.first_name, pre_name)
        self.assertEqual(self.user.email, pre_email)

    def test_to_dict_method(self):
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)

    def test_user_to_dict_output(self):
        dtt = datetime.now()
        dtt_iso = dtt.isoformat()
        my_user = User(
                password="ray223$", id="1423456667286",
                created_at=dtt_iso, updated_at=dtt_iso,
                email="ray@yahoo.com",
                first_name="Ray", last_name="Edward"
                )

        output_dict = {
                "__class__": "User",
                "id": "1423456667286",
                "created_at": dtt_iso,
                "updated_at": dtt_iso,
                "email": "ray@yahoo.com",
                "password": "ray223$",
                "first_name": "Ray",
                "last_name": "Edward"
                }


        self.assertEqual(my_user.to_dict(), output_dict)

    def test_to_dict_output_none(self):
        with self.assertRaises(TypeError):
            self.user.to_dict(None)

if __name__ == "__main__":
    unittest.main()
