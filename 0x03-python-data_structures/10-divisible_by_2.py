#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new = []
    for i in range(int(len(my_list))):
        if my_list[i] % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
