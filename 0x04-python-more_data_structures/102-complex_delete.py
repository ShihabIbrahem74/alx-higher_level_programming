#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    flag = 0
    for i in a_dictionary.values():
        if value == i:
            flag += 1
    for i in range(flag):
        for keys in a_dictionary:
            if a_dictionary[keys] == value:
                del a_dictionary[keys]
                break
    return a_dictionary
