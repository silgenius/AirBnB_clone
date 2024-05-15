#!/usr/bin/python3

""" 
    Module: console

    This module contains the entry point of the command line interpreter interfce CLI
    using HBNB class inherited from Cmd class in cmd module 
"""

import cmd
from models import Storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


 HBNBCommand(cmd.Cmd):
    """this is the HBNB command interpreter."""

    """
    Public instance methods:
    - do_quit(self, line)
    - do_EOF(self, line)
    - do_empty_line(self)
    - do_create(self, line)
    - do_show(self, line)

    Private class attributes:
    - __file_path: string
    - __objects: dictionary
    """
    allcls = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review

    prompt = "(hbnb)"


    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True


    def empty_line():
        """ This line doesn’t execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance, saves it (to the JSON file) and prints the id 
        expected syntax:  create <class name>
        """
        args = line.split()
        cls_name = args[0]
        if not args:
            print("** class name missing **")
        elif cls_name not in self.allcls:
            print("** class doesn't exist **")
        else:
            obj.new = self.allcls[cls_name]()
            obj_new.save()
            print(obj_new.id)


    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id
        expected syntax: show <class name> <id>"""
        args = line.split()
        cls_name = args[0]
        id = args[1]

        if not cls_name:
            print("** class name missing **")
            return None
        elif cls_name not in self.allcls:
            print("** class doesn't exist **")
            return None
        elif len(args) < 2:
                print(** instance id missing **)
            return None
        obj_key = "{}.{}".format(cls_name, id)
        obj_all= models.storage.all()
        if obj_key not in obj_all:
            print("** no instance found **")
        else :
            obj = obj_all[obj_key]
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id and saves the change
        expected syntax: delete <class name> <id>"""
            args = line.split()
            cls_name = ags[0]
            id =args[1]
            if not cls_name:
                print("** class name missing **")
                return None
            elif cls_name not in self.allcls:
                print("** class doesn't exist **")
                return None
            elif len(args) < 2:
                print("** instance id missing **")
                return None 
            obj_key = "{}.{}".format(cls_name, id)
            obj_all = models.storage.all()
                if obj_key not in obj_all:
                    print("** no instance found **")
                else:
                    obj = obj_all[obj_key]
                    del obj
                models.storage.save()


    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name
        >The printed result must be a list of strings
        expected syntax-1: all.
        expected syntax-2: all <class name>"""
            args = line.spilt()
            cls_name = arg[0]
            if cls_name not in self.allcls:
                print("** class doesn't exist **")
                return None
            else:




   def do_update(self, line):
        """ Updates one instance at a call based on the class name and id by adding or updating attribute,
        and saves the change
        expected syntax: update <class name> <id> <attribute name> "<attribute value>" """
        args = line.split()
        cls_name = args[0]
        use_id = args[1]
        attr = args[2]
        attr_value = args[3]
        if not cls_name:
                print("** class name missing **")
                return None
        elif cls_name not in self.allcls:
                print("** class doesn't exist **")
                return None
        elif len(args) < 2:
                print("** instance id missing **")
                return None
        elif len(args) < 3:
                print("** attribute name missing **")
                return None
         elif len(args) < 4:
                print("** value missing **")
                return None
        else:
             obj_key = "{}.{}".format(cls_name, user_id)
            obj_all = models.storage.all()
                if obj_key not in obj_all:
                    print("** no instance found **")
                else :
                    obj = obj_all[obj_key]
                    setattr(obj, attr, attr_value)
                    obj[key].save()



        




if __name__ == '__main__':
    HBNBCommand().cmdloop()
