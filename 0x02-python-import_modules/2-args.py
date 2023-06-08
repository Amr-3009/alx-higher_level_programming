#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv) - 1
    if length == 0:
        print("{:d} argumets.".format(length))
    elif length == 1:
        print("{:d} argument:".format(length))
        print("{:d}: {}".format(length, argv[1]))
    else:
        print("{:d} argumets:".format(length))
        for n in range(1, length + 1):
            print("{:d}: {}".format(n ,argv[n]))
