#!/usr/bin/python3

"""
module that holds a script that creates
an empty list in json file if the file is empty,
then appends python strings gotten from command
line, then saves it in the same json file
"""


import sys
filename = "add_item.json"


def add_object(tfilename):
    """
    function to create an empty list,
    add object to a list and then
    return the list

    Args:
      tfilename: name of json file to to be read from
      args: command line arguments to be appended to a list

    Return:

    """
    if is_file_empty(filename):
        write_file = __import__("1-write_file").write_file
        write_file(filename, "[]")
    else:
        save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
        load_from = __import__("6-load_from_json_file").load_from_json_file
        py_Obj = load_from_json_file(filename)

        for obj in sys.argv[1:]:
            py_Obj.extend(obj)

        save_to_json_file(py_Obj, filename)


def is_file_empty(tfilename):
    """
    Check if a file is empty.

    Args:
        tfilename (str): The name of the file to check.

    Returns:
        bool: True if the file is empty, False otherwise.
    """
    import os
    return os.path.getsize(filename) == 0


add_object(filename)
