def max_integer(list=[]):
    if not isinstance(list, list):
        raise TypeError()
    return max(list)
