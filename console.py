#!/usr/bin/python3

"""
    Module: console

    This module contains the entry point of the command line
    interpreter interfce CLI
    using HBNB class inherited from Cmd class in cmd module
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from parse_string import parse_string


class HBNBCommand(cmd.Cmd):
    """this is the HBNB command interpreter."""

    """
    Public instance methods:
    - do_quit(self, line)
    - do_EOF(self, line)
    - do_empty_line(self)
    - do_create(self, line)
    - do_show(self, line)
    - do_destroy(self, line)
    - do_all(self, line)
    - do_count(self, line)

    Puplic class attributes:
    - allcls
    - prompt
    """

    allcls = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """ This line doesn’t execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance, saves it (to the JSON file)
        and prints the id expected syntax:  create <class name>
        """
        if line:
            args = line.split()
            cls_name = args[0]

        if not args:
            print("** class name missing **")

        elif cls_name not in self.allcls:
            print("** class doesn't exist **")

        else:
            obj_new = self.allcls[cls_name]()
            obj_new.save()
            print(obj_new.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class name and id expected syntax: show <class name> <id>"""
        if line:
            args = line.split()
            if len(args) < 2:
                print("** instance id missing **")
                return

            cls_name = args[0]
            user_id = args[1]
        else:
            print("** class name missing **")
            return

        if cls_name not in self.allcls:
            print("** class doesn't exist **")
            return

        obj_key = "{}.{}".format(cls_name, user_id)
        obj_all = storage.all()
        if obj_key not in obj_all:
            print("** no instance found **")
            return

        obj = obj_all[obj_key]
        print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id and saves the
        change expected syntax: delete <class name> <id>"""
        if line:
            args = line.split()
            if len(args) < 2:
                print("** instance id missing **")
                return

            cls_name = args[0]
            user_id = args[1]
        else:
            print("** class name missing **")
            return

        if cls_name not in self.allcls:
            print("** class doesn't exist **")
            return

        obj_key = "{}.{}".format(cls_name, user_id)
        obj_all = storage.all()
        if obj_key not in obj_all:
            print("** no instance found **")
            return

        obj_all.pop(obj_key)
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or
        not on the class name
        > The printed result must be a list of strings
        expected syntax-1: all.
        expected syntax-2: all <class name>"""
        obj_all = storage.all()
        obj_list = []
        if line:
            args = line.split()
            cls_name = args[0]
            if cls_name not in self.allcls:
                print("** class doesn't exist **")
                return
            else:
                for obj in obj_all.values():
                    if obj.__class__.__name__ == cls_name:
                        obj_list.append(str(obj))
        if not line:
            for obj in obj_all.values():
                obj_list.append(str(obj))

        print(obj_list)

    def do_update(self, line):
        """ Updates one instance at a call based on the class name and
        id by adding or updating attribute, and saves the change
        expected syntax:
            update <class name> <id> <attribute name> "<attribute value>" """
        if line:
            args = line.split()
            cls_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            user_id = args[1]

            if len(args) < 3:
                print("** attribute name missing **")
                return
            attr = args[2]

            if len(args) < 4:
                print("** value missing **")
                return
            attr_value = args[3]
        else:
            print("** class name missing **")
            return

        if cls_name not in self.allcls:
            print("** class doesn't exist **")
            return

        obj_key = "{}.{}".format(cls_name, user_id)
        obj_all = storage.all()
        if obj_key not in obj_all:
            print("** no instance found **")
        else:
            obj = obj_all[obj_key]
            attr_value = attr_value.strip('"')
            if attr_value.isdigit():
                attr_value = int(attr_value)
            setattr(obj, attr, attr_value)
            obj.save()

    def count(self, line):
        """"Retrieves the number of instances of a class
        expected syntax: <class name>.count()"""
        if line:
            cls_name = line
        if not cls_name:
            print("** class name missing **")
            return

        elif cls_name not in self.allcls:
            print("** class doesn't exist **")
            return

        obj_all = storage.all()
        count = 0
        for obj in obj_all.values():
            if obj.__class__.__name__ == cls_name:
                count += 1
        print(count)

    def default(self, line):
        commands = {"destroy": self.do_destroy, "show": self.do_show,
                    "all": self.do_all, "count": self.count,
                    "update": self.do_update}

        command_list = parse_string(line)
        # check if command is in list of special commands
        if command_list == ValueError or command_list[0] not in commands:
            print("*** Unknown syntax: {}".format(line))
            return

        args = ""
        i = 1
        while i < len(command_list):
            if isinstance(command_list[i], str):
                args += command_list[i] + " "
            i += 1
        # Remove extra white space at the end of args
        args = args[:-1]
        # Do these if args is to update an instance from a dictionary
        if len(command_list) == 4 and isinstance(command_list[3], dict):
            for key, value in command_list[3].items():
                string = args[:]
                string += " " + str(key) + " " + str(value)
                self.do_update(string)
            return
        command = commands[command_list[0]]
        command(args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
