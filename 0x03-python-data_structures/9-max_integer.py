#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    num = int(my_list[0])
    for i in range(int(len(my_list))):
        if num < int(my_list[i]):
            num = int(my_list[i])
    return num
