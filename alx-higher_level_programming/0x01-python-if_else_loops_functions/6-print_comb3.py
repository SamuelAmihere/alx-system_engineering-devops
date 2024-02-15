#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if j < i:
            continue
        if j == 9 and i == 8:
            print("{}{}".format(i, j))
            break
        if i != j:
            print("{}{}, ".format(i, j), end="")
