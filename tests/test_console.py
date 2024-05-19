import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


class TestBasicHBNBCommand(unittest.TestCase):
    """ Test Basic HBNB Command """

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            output = f.getvalue()
            self.assertEqual(output, "")

    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            self.assertIn("Documented commands (type help <topic>):", output)

    def test_help_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            output = f.getvalue()
            self.assertEqual(output, "Quit command to exit the program\n\n")

    def test_empty_line(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue()
            self.assertEqual(output, "")

    def EOF_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            output = f.getvalue()
            self.assertEqual(output, "\n")


class TestHBNBCommandCreate(unittest.TestCase):
    """ Test Create command """

    def test_without_classs_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue()
            self.assertEqual(output, "** class name missing **\n")

    def test_with_wrong_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            output = f.getvalue()
            self.assertEqual(output, "** class doesn't exist **\n")

    def test_with_correct_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue()
            self.assertTrue(len(output) > 0)

            # Check if the created instance is saved
            new_instance = storage.all()
            # Remove newline at the end of output
            output = output[:-1]
            new_instance = new_instance["BaseModel.{}".format(output)]
            self.assertIsNotNone(new_instance)


class TestHBNBCommandShow(unittest.TestCase):

    def test_show_no_class_name(self):
        """Test show command with no class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class_name(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_no_id(self):
        """Test show command with no id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_instance_not_found(self):
        """Test show command with valid class name but non-existent id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 121212")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_show_instance(self):
        """Test show command with valid class name and id"""
        # Create a new instance for testing
        instance = BaseModel()
        instance.save()
        instance_id = instance.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {instance_id}")
            output = f.getvalue().strip()
            self.assertIn(f"[BaseModel] ({instance_id})", output)
            self.assertIn(str(instance.__dict__), output)


class TestHBNBCommandDestroy(unittest.TestCase):

    def test_destroy_no_class_name(self):
        """Test destroy command with no class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class_name(self):
        """Test destroy command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_no_id(self):
        """Test destroy command with no id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_instance_not_found(self):
        """Test destroy command with valid class name but non-existent id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_instance(self):
        """Test destroy command with valid class name and id"""
        # Create a new instance for testing
        instance = BaseModel()
        instance.save()
        instance_id = instance.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {instance_id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "")
            # Verify that the instance has been deleted
            self.assertNotIn(f"BaseModel.{instance_id}", storage.all())


class TestHBNBCommandUpdate(unittest.TestCase):
    """ Test update command """

    def setUp(self):
        """Set up a new instance of BaseModel for testing."""
        self.instance = BaseModel()
        self.instance.save()

    def tearDown(self):
        """Clean up by deleting the created instance."""
        storage.all().clear()

    def test_update_no_class_name(self):
        """Test update command with no class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue()
            output = output.strip()
            self.assertEqual(output, "** class name missing **")

    def test_update_invalid_class_name(self):
        """Test update command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            output = f.getvalue()
            output = output.strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_no_id(self):
        """Test update command with no id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            output = f.getvalue()
            output = output.strip()
            self.assertEqual(output, "** instance id missing **")

    def test_update_invalid_id(self):
        """Test update command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 121212")
            output = f.getvalue()
            output = output.strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_no_attribute_name(self):
        """Test update command with valid class name and id
        but no attribute name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {self.instance.id}")
            self.assertEqual(
                    f.getvalue().strip(),
                    "** attribute name missing **"
                    )

    def test_update_no_value(self):
        """Test update command with valid class name and id but no value"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {self.instance.id} name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

    def test_update_valid(self):
        """Test update command with valid class name, id,
        attribute name, and value"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    f'update BaseModel {self.instance.id} name "test_name"'
                    )
            self.assertEqual(f.getvalue().strip(), "")
            updated_instance = storage.all().get(
                    f"BaseModel.{self.instance.id}"
                    )
            self.assertIsNotNone(updated_instance)
            self.assertEqual(updated_instance.name, "test_name")

    def test_update_cast_integer(self):
        """Test update command with an integer value"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    f'update BaseModel {self.instance.id} number 42'
                    )
            self.assertEqual(f.getvalue().strip(), "")
            updated_instance = storage.all().get(
                    f"BaseModel.{self.instance.id}"
                    )
            self.assertIsNotNone(updated_instance)
            self.assertEqual(updated_instance.number, 42)

    def test_update_cast_float(self):
        """Test update command with a float value"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    f'update BaseModel {self.instance.id} price 19.99'
                    )
            self.assertEqual(f.getvalue().strip(), "")
            updated_instance = storage.all().get(
                    f"BaseModel.{self.instance.id}"
                    )
            self.assertIsNotNone(updated_instance)
            self.assertEqual(updated_instance.price, 19.99)


class TestHBNBCommandClassAll(unittest.TestCase):
    """ Test <class name>.all() """
    def setUp(self):
        """Set up instances for testing."""
        self.classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }
        self.instances = {}
        for cls_name, cls in self.classes.items():
            instance = cls()
            instance.save()
            self.instances[cls_name] = instance

    def tearDown(self):
        """Clean up by deleting the created instances."""
        storage.all().clear()

    def test_all_no_class_name(self):
        """Test all command with no class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".all()")
            expected_output = [str(obj) for obj in storage.all().values()]
            self.assertEqual(eval(f.getvalue().strip()), expected_output)

    def test_all_invalid_class_name(self):
        """Test all command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.all()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_all_valid_class_name(self):
        """Test all command with valid class name"""
        for cls_name, instance in self.instances.items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"{cls_name}.all()")
                expected_output = [
                        str(obj)
                        for key, obj in storage.all().items()
                        if key.startswith(cls_name)
                        ]
                self.assertEqual(eval(f.getvalue().strip()), expected_output)


class TestHBNBCommandClassCount(unittest.TestCase):
    """ Test for <class name>.count() """

    def setUp(self):
        """Set up instances for testing."""
        self.classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }
        self.instances = {}
        for cls_name, cls in self.classes.items():
            for _ in range(3):  # Creating 3 instances for each class
                instance = cls()
                instance.save()
                self.instances.setdefault(cls_name, []).append(instance)

    def tearDown(self):
        """Clean up by deleting the created instances."""
        storage.all().clear()

    def test_count_invalid_class_name(self):
        """Test count command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.count()")
            self.assertEqual(
                    f.getvalue().strip(),
                    "** class doesn't exist **"
                    )

    def test_count_valid_class_name(self):
        """Test count command with valid class name"""
        for cls_name, instances in self.instances.items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"{cls_name}.count()")
                self.assertEqual(f.getvalue().strip(), str(len(instances)))


class TestHBNBCommandClassShow(unittest.TestCase):
    """ Test for <class name>.show(<id>) """

    def setUp(self):
        """Set up instances for testing."""
        self.classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }
        self.instances = {}
        for cls_name, cls in self.classes.items():
            instance = cls()
            instance.save()
            self.instances[cls_name] = instance

    def tearDown(self):
        """Clean up by deleting the created instances."""
        storage.all().clear()

    def test_show_invalid_class_name(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.show(1234-1234-1234)")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_no_id(self):
        """Test show command with no id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_instance_not_found(self):
        """Test show command with an id that does not exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(1234-1234-1234)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_show_valid_instance(self):
        """Test show command with a valid class name and id"""
        for cls_name, instance in self.instances.items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"{cls_name}.show(\"{instance.id}\")")
                expected_output = str(
                        storage.all()[f"{cls_name}.{instance.id}"]
                        )
                self.assertEqual(f.getvalue().strip(), expected_output)


class TestHBNBCommandClassDestroy(unittest.TestCase):
    """ Test for <class name>.destroy(<id>) """

    def setUp(self):
        """Set up instances for testing."""
        self.classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }
        self.instances = {}
        for cls_name, cls in self.classes.items():
            instance = cls()
            instance.save()
            self.instances[cls_name] = instance

    def tearDown(self):
        """Clean up by deleting the created instances."""
        storage.all().clear()

    def test_destroy_invalid_class_name(self):
        """Test destroy command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.destroy(1234-1234-1234)")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_no_id(self):
        """Test destroy command with no id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_instance_not_found(self):
        """Test destroy command with an id that does not exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(1234-1234-1234)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_valid_instance(self):
        """Test destroy command with a valid class name and id"""
        for cls_name, instance in self.instances.items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"{cls_name}.destroy(\"{instance.id}\")")
                self.assertNotIn(instance, storage.all().values())
                self.assertEqual(f.getvalue().strip(), "")


class TestHBNBCommandClassUpdate(unittest.TestCase):
    """ Test for <class name>.update(<id>, <dictionary representation>) """

    def setUp(self):
        """Set up instances for testing."""
        self.classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }
        self.instances = {}
        for cls_name, cls in self.classes.items():
            instance = cls()
            instance.save()
            self.instances[cls_name] = instance

    def tearDown(self):
        """Clean up by deleting the created instances."""
        storage.all().clear()

    def test_update_no_class_name(self):
        """Test update command with no class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".update()")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class_name(self):
        """Test update command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    "MyModel.update(\"1234-1234-1234\", \"name\", \"value\")"
                    )
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_no_id(self):
        """Test update command with no id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_instance_not_found(self):
        """Test update command with an id that does not exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    "BaseModel.update(\"1234-1234-1234\", \"name\", \"value\")"
                    )
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_no_attribute_name(self):
        """Test update command with no attribute name"""
        for cls_name, instance in self.instances.items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"{cls_name}.update(\"{instance.id}\")")
                self.assertEqual(
                        f.getvalue().strip(),
                        "** attribute name missing **"
                        )

    def test_update_no_value(self):
        """Test update command with no value"""
        for cls_name, instance in self.instances.items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(
                        f"{cls_name}.update(\"{instance.id}\", \"name\")"
                        )
                self.assertEqual(f.getvalue().strip(), "** value missing **")

    def test_update_valid_instance(self):
        """Test update command with a valid class name, id,
        attribute name, and value"""
        for cls_name, instance in self.instances.items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(
                        f"{cls_name}.update("
                        f"\"{instance.id}\", "
                        f"\"name\", "
                        f"\"Ray\")"
                        )
                updated_instance = storage.all()[f"{cls_name}.{instance.id}"]
                self.assertEqual(updated_instance.name, 'Ray')
                self.assertEqual(f.getvalue().strip(), "")


class TestHBNBCommandUpdateWithDict(unittest.TestCase):

    def setUp(self):
        """Set up instances for testing."""
        self.classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }
        self.instances = {}
        for cls_name, cls in self.classes.items():
            instance = cls()
            instance.save()
            self.instances[cls_name] = instance

    def tearDown(self):
        """Clean up by deleting the created instances."""
        storage.all().clear()

    def test_update_no_class_name(self):
        """Test update command with no class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".update()")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class_name(self):
        """Test update command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.update()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_no_id(self):
        """Test update command with no id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_instance_not_found(self):
        """Test update command with valid class name but non-existent id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(121212)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_valid_instance_with_dict(self):
        """Test update command with valid class name, id, and dictionary"""
        update_dict = '{"name": "Holberton", "age": 89}'
        for cls_name, instance in self.instances.items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(
                        f'{cls_name}.update(\"{instance.id}\", {update_dict})'
                        )
                self.assertEqual(f.getvalue().strip(), "")
                updated_instance = storage.all()[f"{cls_name}.{instance.id}"]
                self.assertEqual(updated_instance.name, "Holberton")
                self.assertEqual(updated_instance.age, 89)


class TestHBNBCommandDefault(unittest.TestCase):
    """ Test invalid command """
    def test_invalid_command(self):
        """Test default behavior for invalid command"""
        invalid_commands = [
            "unknown_command",
            "wroong",
            "right",
            "123443",
            "invalid.command",
            "User"
            "some_random_text"
        ]

        for command in invalid_commands:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(command)
                self.assertEqual(
                        f.getvalue().strip(), "*** Unknown syntax: " + command
                        )


if __name__ == '__main__':
    unittest.main()
