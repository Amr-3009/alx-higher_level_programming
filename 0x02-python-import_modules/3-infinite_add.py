#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    sum = 0
    for n in range(1, length):
        sum = sum + int(argv[n])
    print("{}".format(sum))
