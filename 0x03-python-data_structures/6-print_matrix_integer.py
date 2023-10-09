#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    flag = 0
    if not matrix:
        return
    leng = len(matrix)
    for i in range(leng):
        if int(len(matrix[i])) == 0:
            print("")
        for x in range(int(len(matrix[i]))):
            print("{:d}".format(matrix[i][x]),
                  end='\n' if x == len(matrix[i]) - 1 else " ")
