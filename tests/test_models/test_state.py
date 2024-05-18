#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep
import os

class TestStateParentClass(unittest.TestCase):
    """Test cases for State class parent that inherited from BaseModel"""
    
    def test_StateParentClass(self):
        self.assertIsInstance(State(), BaseModel)


class TestStateInstances(unittest.TestCase):
    """Test for instances of State class with different cases"""

    def setUp(self):
        self.my_state = State()

    def test_with_args_and_kwargs(self):
        dtt = datetime.now()
        dtt_iso = dtt.isoformat()
        my_state = State(
            "18", id="2314564356345",
            created_at=dtt_iso, updated_at=dtt_iso,
            name="California"
        )
        self.assertEqual(my_state.id, "2314564356345")
        self.assertEqual(my_state.created_at, dtt)
        self.assertEqual(my_state.updated_at, dtt)
        self.assertEqual(my_state.name, "California")

    def test_with_None_args_kwargs(self):
        my_state = State(None)
        self.assertNotIn(None, my_state.__dict__.values())


class TestStateUnique(unittest.TestCase):
    """Test cases for each state attribute in State class"""

    def setUp(self):
        self.state1 = State()
        sleep(0.01)
        self.state2 = State()

    def test_unique_id(self):
        self.assertNotEqual(self.state1.id, self.state2.id)

    def test_unique_timestamps_created_at(self):
        self.assertLess(self.state1.created_at, self.state2.created_at)


class TestStateAttrTypes(unittest.TestCase):
    """Test cases for types of attributes of State in State class"""

    def setUp(self):
        self.my_state = State()

    def test_State_id_type(self):
        self.assertIs(type(self.my_state.id), str)

    def test_State_name_type(self):
        self.assertIs(type(self.my_state.name), str)

    def test_State_created_at_instance(self):
        self.assertIsInstance(self.my_state.created_at, datetime)
        iso_str = self.my_state.created_at.isoformat()
        self.assertIsInstance(iso_str, str)


class TestStateMethods(unittest.TestCase):
    """Test cases for different methods on State instance of State class"""

    def setUp(self):
        self.my_state = State()
        
    def test_save_method_changed_value(self):
        pre_updated_at = self.my_state.updated_at
        self.my_state.save()
        self.assertGreater(self.my_state.updated_at, pre_updated_at)


class TestStateSerialization(unittest.TestCase):
    """Test cases for serialization and deserialization of State class"""

    def setUp(self):
        """Set up for testing"""
        self.state = State()

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

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
