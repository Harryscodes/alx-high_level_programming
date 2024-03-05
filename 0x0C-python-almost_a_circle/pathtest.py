import os
import sys

print(__file__)

path = os.path.dirname(__file__)

print()
print(sys.path)
print()
print('path by os.path.dirname' +'\n')
print(path)

print('path by os.path.join with ".."' +'\n')
print(os.path.join(path, '../..'))
print('\n\n\n')
print(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(path, '../..')))
print(sys.path)
