import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel

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


class TestHBNBCreateCommand(unittest.TestCase):
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
