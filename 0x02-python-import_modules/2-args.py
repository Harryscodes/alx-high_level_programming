#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    msg = "argument" if len(sys.argv) == 2 else "arguments"
    point = '.' if len(sys.argv) == 1 and len(sys.argv) != 2 else ':'
    print("{:d} {:s}{}".format(len(sys.argv) - 1, msg, point))
    for i in range(len(sys.argv[1:])):
        print("{:d}: {:s}".format(i+1, sys.argv[i+1]))
