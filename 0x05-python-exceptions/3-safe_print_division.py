#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        print("Inside result: {:.1f}".format(result))
    finally:
        return result
