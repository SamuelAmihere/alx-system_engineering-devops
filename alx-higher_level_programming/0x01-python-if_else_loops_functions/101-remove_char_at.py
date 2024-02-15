#!/usr/bin/python3
def remove_char_at(str, n):
    if n > 0:
        str1 = str[0:n]
        str2 = str[n + 1:]
        return (str1[0:] + str2[0:])
    elif n == 0:
        return (str[1:])
    else:
        return (str)
