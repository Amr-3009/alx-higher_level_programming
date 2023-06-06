#!/usr/bin/python3
for n in range(97, 123):
    if chr(n) == "q" or chr(n) == "e":
        continue
    else:
        print("{}".format(chr(n)), end="")
