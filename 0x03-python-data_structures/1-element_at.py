#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list) - 1:
        return
    if my_list[idx] < 0:
        return
    return (my_list[idx])
