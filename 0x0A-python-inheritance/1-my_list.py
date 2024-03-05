#!/usr/bin/python3

"""
module that houses a class that inherits from a list
"""


class MyList(list):

    """
    MyList class that inherits from python list class
    """
    def print_sorted(self):
        """
        public method to print the sorted version
        of MyList object
        """
        print(sorted(self))
