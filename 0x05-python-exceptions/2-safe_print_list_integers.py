#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    flag = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except Exception:
            continue
        flag = flag + 1
    print("".format())
    return (flag)
