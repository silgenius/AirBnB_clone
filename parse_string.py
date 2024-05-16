#!/usr/bin/python3

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
