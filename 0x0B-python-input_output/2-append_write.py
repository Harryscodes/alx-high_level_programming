#!/usr/bin/python3

"""
module to houses a function
that writes to a file and returns
number of characters written to the file
"""


def append_write(filename="", text=""):
    """
    append_write - function that append to a file and returns
    number of characters appended to the file

    Args:
       filename: name of file to be written to. it gets
       created if it does not exist or overwrites
       file if file exist

    Return:
       number of characters written to file
    """
    count = 0
    with open(filename, 'a', encoding='UTF8') as f:
        count = f.write(text)

    return count
