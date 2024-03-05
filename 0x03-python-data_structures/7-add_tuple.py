#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    return a the result of summing tuple_a and tuple_b

    tuple_a: a tuple , if len(tuple_a) < 1, add 0 as
    other elements of tuple_a

    tuple_b: a tuple, if len(tuple_b) < 1, add 0 as
    other elements of tuple_b
    """

    num = []

    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        for i in range(2):
            num.append(tuple_a[i] + tuple_b[i])
        return tuple(num)
    else:
        if len(tuple_a) < 2:
            tuple_a = list(tuple_a)
            while len(tuple_a) != 2:
                tuple_a.append(0)
        if len(tuple_b) < 2:
            tuple_b = list(tuple_b)
            while len(tuple_b) != 2:
                tuple_b.append(0)

        for i in range(2):
            num.append(tuple_a[i] + tuple_b[i])
        return tuple(num)
