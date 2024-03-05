#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
print(dir(s.__class__))
print(s.__reduce__)
