#!/usr/bin/python3

def print_last_digit(number):
    last_digit = int(f"{str(number)[-1]}")
    print(f"{last_digit:d}", end="")
    return last_digit
