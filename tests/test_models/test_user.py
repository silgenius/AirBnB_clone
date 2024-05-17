#!/usr/bin/python3

"""This user instance class test file """


import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from time import sleep

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

    def test_with_None_args(self):
        my_user = User(
            "22", id=None,
            created_at=None, updated_at=None,
            email=None, password=None,
            first_name=None, last_name=None
            )

        self.assertNotIn(None, my_user.__dict__.values())


class TestUserUnique(unittest.TestCase):
        """Test cases for each user attributes in user class"""

        def setUp(self):
            self.user1 = User()
            sleep(0.01)
            self.user2 = User()

        def test_unique_id(self):
            self.assertNotEqual(self.user1.id, self.user2.id)

        def test_unique_id(self):
            self.assertNotEqual(self.user1.email, self.user2.email)

        def test_unique_created_at(self):
            self.assertLess(
                self.user1.created_at, self.user2.created_at
                )


class TestUserAttrTypes(unittest.TestCase):
    """Test cases for types of attributes of user in user class"""
    def setUp(self):
            self.my_user = User()

    def test_User_id_type(self):
        self.assertIs(type(my_user.id), str)

    def test_User_first_name_type(self):
        self.assertIs(type(my_user.first_name), str)

    def test_User_last_name_type(self):
        self.assertIs(type(my_user.last_name), str)

    def test_User_email_type(self):
        self.assertIs(type(my_user.email), str)

    def test_User_password_type(self):
        self.assertIs(type(my_user.password), str)

    def test_User_created_at_instance(self):
        self.assertIsInstance(my_user.created_at, datetime)
        iso_str = my_user.created_at.isoformat()
        self.assertIsInstance(iso_str, str)



class TestUserMethods(unittest.TestCase):
    """test cases for different methods on user instance of user class"""

    def test_save_method_changed_vlaue(self):
    pre_updated_at = self.user.updated_at
    self.user.models.save()
    self.assertNotEqual(pre_updated_at, self.user.updated_at)





if __name__ == '__main__':
    unittest.main()



