#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        cnt = 0
        for j in i:
            cnt += 1
            print("{:d}{}".format(
                j,
                "" if cnt == len(i) else " "), end="")
        print("")
