#!/usr/bin/python3
def no_c(my_string):
    new = ""
    leng = len(my_string)
    for i in range(leng):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            new = new + my_string[i]
    return new
