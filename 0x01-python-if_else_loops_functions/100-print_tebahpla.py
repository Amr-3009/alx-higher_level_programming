#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 != 0:
        i = 32
    else:
        i = 0
    print("{}".format(chr(c - i)), end="")
