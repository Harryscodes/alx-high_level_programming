#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        return
    count = 0
    for i in range(x):
        # if isinstance(i, int):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
