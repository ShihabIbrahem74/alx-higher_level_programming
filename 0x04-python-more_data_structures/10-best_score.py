#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    name = ""
    big = 0
    for i in a_dictionary:
        if big < a_dictionary[i]:
            name = i
            big = a_dictionary[i]
    return name
