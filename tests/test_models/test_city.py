#!/usr/bin/python3

"""This city instance class test file with different test cases"""


import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
from time import sleep

class TestCityParentClass(unittest.TestCase):
    """test cases for city class parent that inherited from """
    def test_CityParentClass(self):
        self.assertIsInstance(City(), BaseModel)


class TestCityInstances(unittest.TestCase):
    """test for instances of city class with different cases"""

    def setUp(self):
        self.my_city = City()

    def test_with_args_and_kwargs(self):
        dtt = datetime.now()
        dtt_iso = dtt.isoformat()
        City(
            "18", id="2314564356345",
            created_at=dtt_iso, updated_at=dtt_iso,
            state_id="370", name="Alex"
        )
        self.assertEqual(my_user.id, "2314564356345")
        self.assertEqual(my_user.created_at, dtt)
        self.assertEqual(my_user.updated_at, dtt)
        self.assertEqual(my_user.state_id, "370")
        self.assertEqual(my_user.name, "Alex")

    def test_with_None_args_kwargs(self):
        my_city = City(None)

        self.assertNotIn(None, my_city.__dict__.values())


class TestCityUnique(unittest.TestCase):
        """Test cases for each city attributes in city class"""

        def setUp(self):
            self.city1 = City()
            sleep(0.01)
            self.city2 = City()

        def test_unique_id(self):
            self.assertNotEqual(self.city1.id, self.city2.id)

        
        def test_unique_timestamps_created_at(self):
            self.assertLess(
                self.city1.created_at, self.city2.created_at
            )

class TestCityAttrTypes(unittest.TestCase):
        """Test cases for types of attributes of city in city class"""
        def setUp(self):
            self.my_city = City()

        def test_City_id_type(self):
            self.assertIs(type(self.my_city.id), str)

        def test_City_first_name_type(self):
            self.assertIs(type(self.my_city.state_id), str)

        def test_City_last_name_type(self):
            self.assertIs(type(self.my_city.name), str)


        def test_City_created_at_instance(self):
            self.assertIsInstance(self.my_city.created_at, datetime)
            iso_str = self.my_city.created_at.isoformat()
            self.assertIsInstance(iso_str, str)

    class TestCityMethods(unittest.TestCase):
        """test cases for different methods on user instance of user class"""
        def setUp(self):
            self.my_city = City()
        
        def test_save_method_changed_value(self):
            pre_updated_at = self.my_city.updated_at
            self.my_city.models.save()
            self.assertGreater(self.my_city.updated_at, pre_updated_at)

        def test_to_dict_method_changed_value(self):







if __name__ == '__main__':
    unittest.main()


