#!/usr/bin/python3


import unittest
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep
import os

class TestCityParentClass(unittest.TestCase):
    """Test cases for City class parent that it inherited from BaseModel"""
    
    def test_CityParentClass(self):
        self.assertIsInstance(City(), BaseModel)


class TestCityInstances(unittest.TestCase):
    """Test for instances of City class with different cases"""

    def setUp(self):
        self.my_city = City()

    def test_with_args_and_kwargs(self):
        dtt = datetime.now()
        dtt_iso = dtt.isoformat()
        my_city = City(
            "18", id="2314564356345",
            created_at=dtt_iso, updated_at=dtt_iso,
            state_id="370", name="Alex"
        )
        self.assertEqual(my_city.id, "2314564356345")
        self.assertEqual(my_city.created_at, dtt)
        self.assertEqual(my_city.updated_at, dtt)
        self.assertEqual(my_city.state_id, "370")
        self.assertEqual(my_city.name, "Alex")

    def test_with_None_args_kwargs(self):
        my_city = City(None)
        self.assertNotIn(None, my_city.__dict__.values())


class TestCityUnique(unittest.TestCase):
    """Test cases for each city attribute in City class"""

    def setUp(self):
        self.city1 = City()
        sleep(0.01)
        self.city2 = City()

    def test_unique_id(self):
        self.assertNotEqual(self.city1.id, self.city2.id)

    def test_unique_timestamps_created_at(self):
        self.assertLess(self.city1.created_at, self.city2.created_at)


class TestCityAttrTypes(unittest.TestCase):
    """Test cases for types of attributes of City in City class"""

    def setUp(self):
        self.my_city = City()

    def test_City_id_type(self):
        self.assertIs(type(self.my_city.id), str)

    def test_City_state_id_type(self):
        self.assertIs(type(self.my_city.state_id), str)

    def test_City_name_type(self):
        self.assertIs(type(self.my_city.name), str)

    def test_City_created_at_instance(self):
        self.assertIsInstance(self.my_city.created_at, datetime)
        iso_str = self.my_city.created_at.isoformat()
        self.assertIsInstance(iso_str, str)


class TestCityMethods(unittest.TestCase):
    """Test cases for different methods on City instance of City class"""

    def setUp(self):
        self.my_city = City()
        
    def test_save_method_changed_value(self):
        pre_updated_at = self.my_city.updated_at
        self.my_city.save()
        self.assertGreater(self.my_city.updated_at, pre_updated_at)


class TestCitySerialization(unittest.TestCase):
    """Test cases for serialization and deserialization of City class"""

    def setUp(self):
        """Set up for testing"""
        self.city = City()

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_city_serialization(self):
        """Test if City can be serialized and deserialized correctly"""
        storage = FileStorage()
        storage.new(self.city)
        storage.save()
        
        storage.reload()
        city_key = f"City.{self.city.id}"
        self.assertIn(city_key, storage.all())

        deserialized_city = storage.all()[city_key]
        self.assertEqual(deserialized_city.state_id, "")
        self.assertEqual(deserialized_city.name, "")


if __name__ == "__main__":
    unittest.main()

