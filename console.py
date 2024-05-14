#!/usr/bin/python3

    """ This module contains the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """this is the HBNB command interpreter."""

    prompt = "(hbnb)"


    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True


    def empty_line():
        """empty line shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
