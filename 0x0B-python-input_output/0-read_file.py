#!/usr/bin/python3

"""
module that houses a function that
reads the content of a file
"""


def read_file(filename=""):
    """
    read_file: function to read content of a file
    Args:
       filename: name of file to be read from
    Return: None is returned
    """
    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read(), end="")
