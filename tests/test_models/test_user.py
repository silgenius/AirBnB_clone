#!/usr/bin/python3

"""This user instance class test file """


import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUserInstances(unittest.TestCase):
    """test for instances of user class setup 2 users then test them in different cases"""

    def setUp(self):
        self.user1 = User()
        self.user2 = User()

    def test_with_args_and_kwargs(self):
        dtt = datetime.now()
        date_iso = dtt.isoformat()
        user = User(
            "22", id="1423456667286",
            created_at=date_iso, updated_at=date_iso,
            email="ray@yahoo.com", password="ray223$",
            first_name="Ray", last_name="Edward"
        )

        self.assertEqual(user.id, "1423456667286")
        self.assertEqual(user.created_at, date)
        self.assertEqual(user.updated_at, date)
        self.assertEqual(user.email, "ray@yahoo.com")
        self.assertEqual(user.password, "ray223$")
        self.assertEqual(user.first_name, "Ray")
        self.assertEqual(user.last_name, "Edward")



if __name__ == '__main__':
    unittest.main()



