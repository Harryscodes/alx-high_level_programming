#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as c

    if len(sys.argv[1:]) != 3:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        sys.exit(1)

    operations = ["+", "-", "*", "/"]

    if sys.argv[2] in operations:

        operation = operations.index(sys.argv[2])

        a1 = int(sys.argv[1])
        a2 = sys.argv[2]
        a3 = int(sys.argv[3])

        if operation == 0:
            print("{} {} {} = {}".format(a1, a2, a3, c.add(a1, a3)))
        elif operation == 1:
            print("{} {} {} = {}".format(a1, a2, a3, c.sub(a1, a3)))
        elif operation == 2:
            print("{} {} {} = {}".format(a1, a2, a3, c.mul(a1, a3)))
        else:
            print("{} {} {} = {}".format(a1, a2, a3, c.div(a1, a3)))
    else:
        print(f"Unknown operator. Available operators: +, -, * and / ")
        sys.exit(1)
