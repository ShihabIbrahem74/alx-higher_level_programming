#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 96 and ord(c) <= 122:
            i = ord(c) - 32
            c = chr(i)
        print("{}".format(c), end="")
    print("".format())
