#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        num = ord(str[i])
        if num in range(97, 123):
            if i < len(str) - 1:
                end = ""
            else:
                end = "\n"
            print("{:c}".format(num - 32), end=end)
        else:
            if i < len(str) - 1:
                end = ""
            else:
                end = "\n"
            print("{:c}".format(num), end=end)
