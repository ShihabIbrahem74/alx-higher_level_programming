#!/usr/bin/python3
for ten in range(9):
    for one in range(ten + 1, 10):
        if one == ten:
            continue
        if one == 9 and ten == 8:
            print("{}{}".format(ten, one))
        else:
            print("{}{}, ".format(ten, one), end="")
