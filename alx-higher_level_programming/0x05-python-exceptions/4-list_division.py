#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    temp, n = [], 0
    result = 0

    while (n < list_length):
        try:
            result = my_list_1[n] / my_list_2[n]
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        finally:
            temp.append(result)
        n += 1
    return (temp)
