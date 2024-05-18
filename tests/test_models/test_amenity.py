#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep
import os

class TestAmenityParentClass(unittest.TestCase):
    """Test cases for Amenity class parent that it inherited from BaseModel"""
    
    def test_AmenityParentClass(self):
        self.assertIsInstance(Amenity(), BaseModel)


class TestAmenityInstances(unittest.TestCase):
    """Test for instances of Amenity class with different cases"""

    def setUp(self):
        self.my_amenity = Amenity()

    def test_with_args_and_kwargs(self):
        dtt = datetime.now()
        dtt_iso = dtt.isoformat()
        my_amenity = Amenity(
            "18", id="2314564356345",
            created_at=dtt_iso, updated_at=dtt_iso,
            name="Pool"
        )
        self.assertEqual(my_amenity.id, "2314564356345")
        self.assertEqual(my_amenity.created_at, dtt)
        self.assertEqual(my_amenity.updated_at, dtt)
        self.assertEqual(my_amenity.name, "Pool")

    def test_with_None_args_kwargs(self):
        my_amenity = Amenity(None)
        self.assertNotIn(None, my_amenity.__dict__.values())


class TestAmenityUnique(unittest.TestCase):
    """Test cases for each amenity attribute in Amenity class"""

    def setUp(self):
        self.amenity1 = Amenity()
        sleep(0.01)
        self.amenity2 = Amenity()

    def test_unique_id(self):
        self.assertNotEqual(self.amenity1.id, self.amenity2.id)

    def test_unique_timestamps_created_at(self):
        self.assertLess(self.amenity1.created_at, self.amenity2.created_at)


class TestAmenityAttrTypes(unittest.TestCase):
    """Test cases for types of attributes of Amenity in Amenity class"""

    def setUp(self):
        self.my_amenity = Amenity()

    def test_Amenity_id_type(self):
        self.assertIs(type(self.my_amenity.id), str)

    def test_Amenity_name_type(self):
        self.assertIs(type(self.my_amenity.name), str)

    def test_Amenity_created_at_instance(self):
        self.assertIsInstance(self.my_amenity.created_at, datetime)
        iso_str = self.my_amenity.created_at.isoformat()
        self.assertIsInstance(iso_str, str)


class TestAmenityMethods(unittest.TestCase):
    """Test cases for different methods on Amenity instance of Amenity class"""

    def setUp(self):
        self.my_amenity = Amenity()
        
    def test_save_method_changed_value(self):
        pre_updated_at = self.my_amenity.updated_at
        self.my_amenity.save()
        self.assertGreater(self.my_amenity.updated_at, pre_updated_at)


class TestAmenitySerialization(unittest.TestCase):
    """Test cases for serialization and deserialization of Amenity class"""

    def setUp(self):
        """Set up for testing"""
        self.amenity = Amenity()

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_amenity_serialization(self):
        """Test if Amenity can be serialized and deserialized correctly"""
        storage = FileStorage()
        storage.new(self.amenity)
        storage.save()
        
        storage.reload()
        amenity_key = f"Amenity.{self.amenity.id}"
        self.assertIn(amenity_key, storage.all())

        deserialized_amenity = storage.all()[amenity_key]
        self.assertEqual(deserialized_amenity.name, "")


if __name__ == "__main__":
    unittest.main()

