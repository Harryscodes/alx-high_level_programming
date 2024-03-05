#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            # Try to perform the division
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            # Handle if elements are not integers or floats
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result = 0
        except IndexError:
            # Handle if lists are too short
            print("out of range")
            result = 0
        finally:
            # Append the result to the result_list
            result_list.append(result)

    return result_list
