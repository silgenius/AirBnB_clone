#!/usr/bin/python3

import unittest
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep
import os

class TestPlaceParentClass(unittest.TestCase):
    """Test cases for Place class parent that it inherited from BaseModel"""
    
    def test_PlaceParentClass(self):
        self.assertIsInstance(Place(), BaseModel)


class TestPlaceInstances(unittest.TestCase):
    """Test for instances of Place class with different cases"""

    def setUp(self):
        self.my_place = Place()

    def test_with_args_and_kwargs(self):
        dtt = datetime.now()
        dtt_iso = dtt.isoformat()
        my_place = Place(
            "18", id="2314564356345",
            created_at=dtt_iso, updated_at=dtt_iso,
            city_id="1", user_id="2", name="Lovely House",
            description="A cozy place", number_rooms=2,
            number_bathrooms=1, max_guest=4, price_by_night=100,
            latitude=40.7128, longitude=-74.0060,
            amenity_ids=["1", "2"]
        )
        self.assertEqual(my_place.id, "2314564356345")
        self.assertEqual(my_place.created_at, dtt)
        self.assertEqual(my_place.updated_at, dtt)
        self.assertEqual(my_place.city_id, "1")
        self.assertEqual(my_place.user_id, "2")
        self.assertEqual(my_place.name, "Lovely House")
        self.assertEqual(my_place.description, "A cozy place")
        self.assertEqual(my_place.number_rooms, 2)
        self.assertEqual(my_place.number_bathrooms, 1)
        self.assertEqual(my_place.max_guest, 4)
        self.assertEqual(my_place.price_by_night, 100)
        self.assertEqual(my_place.latitude, 40.7128)
        self.assertEqual(my_place.longitude, -74.0060)
        self.assertEqual(my_place.amenity_ids, ["1", "2"])

    def test_with_None_args_kwargs(self):
        my_place = Place(None)
        self.assertNotIn(None, my_place.__dict__.values())


class TestPlaceUnique(unittest.TestCase):
    """Test cases for each place attribute in Place class"""

    def setUp(self):
        self.place1 = Place()
        sleep(0.01)
        self.place2 = Place()

    def test_unique_id(self):
        self.assertNotEqual(self.place1.id, self.place2.id)

    def test_unique_timestamps_created_at(self):
        self.assertLess(self.place1.created_at, self.place2.created_at)


class TestPlaceAttrTypes(unittest.TestCase):
    """Test cases for types of attributes of Place in Place class"""

    def setUp(self):
        self.my_place = Place()

    def test_Place_id_type(self):
        self.assertIs(type(self.my_place.id), str)

    def test_Place_city_id_type(self):
        self.assertIs(type(self.my_place.city_id), str)

    def test_Place_user_id_type(self):
        self.assertIs(type(self.my_place.user_id), str)

    def test_Place_name_type(self):
        self.assertIs(type(self.my_place.name), str)

    def test_Place_description_type(self):
        self.assertIs(type(self.my_place.description), str)

    def test_Place_number_rooms_type(self):
        self.assertIs(type(self.my_place.number_rooms), int)

    def test_Place_number_bathrooms_type(self):
        self.assertIs(type(self.my_place.number_bathrooms), int)

    def test_Place_max_guest_type(self):
        self.assertIs(type(self.my_place.max_guest), int)

    def test_Place_price_by_night_type(self):
        self.assertIs(type(self.my_place.price_by_night), int)

    def test_Place_latitude_type(self):
        self.assertIs(type(self.my_place.latitude), float)

    def test_Place_longitude_type(self):
        self.assertIs(type(self.my_place.longitude), float)

    def test_Place_amenity_ids_type(self):
        self.assertIs(type(self.my_place.amenity_ids), list)

    def test_Place_created_at_instance(self):
        self.assertIsInstance(self.my_place.created_at, datetime)
        iso_str = self.my_place.created_at.isoformat()
        self.assertIsInstance(iso_str, str)


class TestPlaceMethods(unittest.TestCase):
    """Test cases for different methods on Place instance of Place class"""

    def setUp(self):
        self.my_place = Place()
        
    def test_save_method_changed_value(self):
        pre_updated_at = self.my_place.updated_at
        self.my_place.save()
        self.assertGreater(self.my_place.updated_at, pre_updated_at)


class TestPlaceSerialization(unittest.TestCase):
    """Test cases for serialization and deserialization of Place class"""

    def setUp(self):
        """Set up for testing"""
        self.place = Place()

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_place_serialization(self):
        """Test if Amenity can be serialized and deserialized correctly"""
        storage = FileStorage()
        storage.new(self.place)
        storage.save()
        
        storage.reload()
        place_key = f"Place.{self.place.id}"
        self.assertIn(place_key, storage.all())

        deserialized_place = storage.all()[place_key]
        self.assertEqual(deserialized_place.name, "")


if __name__ == "__main__":
    unittest.main()
