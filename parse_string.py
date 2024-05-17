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


def parse_string(line):
    my_list = []
    try:
        cls_name, content = line.split(".")
        command, args = content.split("(")
    except ValueError:
        return ValueError
    my_list.append(command)
    my_list.append(cls_name)
    if args[-1] == ")":
        args = args[:-1]
    if args:
        type_args = eval(args)
        if isinstance(type_args, tuple):
            for i in type_args:
                my_list.append(i)
        else:
            if "\"" in args:
                args = args[1:-1]
            my_list.append(args)

    return my_list
