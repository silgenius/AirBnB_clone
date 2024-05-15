#!/usr/bin/python3

def do_count(self, line):
    """"Retrieves the number of instances of a class
    expected syntax: <class name>.count()"""
    if line:
        cls_name = line.split('.')[0]
        if not cls_name:
            print("** class name missing **")
            return None

        elif cls_name not in self.allcls:
            print("** class doesn't exist **")
            return None

    obj_all = models.storage.all()
    count = 0
    for obj in obj_all.values():
        if obj.__class__.__name__ == cls_name:
            count += 1
    print(count)
    return count
