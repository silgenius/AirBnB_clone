#!/usr/bin/python3

"""
    Parses a string containing a command in the format
    'class_name.method(args)'.

    Parameters:
        line (str): The string to parse.

    Returns:
        list or ValueError: A list containing the parsed components
        [command, class_name, *args], or a ValueError if the input
        string does not match the expected format.
"""

from ast import literal_eval


def parse_string(line):
    my_list = []
    try:
        cls_name, content = line.split(".", 1)
        command, args = content.split("(", 1)
    except ValueError:
        return ValueError
    my_list.append(command)
    my_list.append(cls_name)
    if args and args[-1] == ")":
        args = args[:-1]
    else:
        return ValueError

    if "," in args:
        # Re-format args
        args = f'({args})'
        args = literal_eval(args)
        for arg in args:
            my_list.append(arg)
    else:
        args = args[1:-1]
        my_list.append(args)

    return my_list
