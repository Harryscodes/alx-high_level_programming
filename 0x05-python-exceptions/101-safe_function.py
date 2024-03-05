#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        a, b = args[0], args[1]
        return fct(a, b)
    except (ZeroDivisionError, IndexError, NameError) as e:
        print("{} {}".format("Exception:", e), file=sys.stderr)
