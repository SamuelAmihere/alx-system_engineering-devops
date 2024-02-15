#!/usr/bin/python3
"""Finds a peak-finding algorithm.
"""


def find_peak(list_of_integers):
    """Finds peak of list_of_integers or None
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]

    mid = int(size / 2)

    while True:
        size = int(size / 2)
        if size > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if int(size / 2) == 0:
                mid = 2
            mid = mid - int(size / 2)
        elif (mid < size - 1 and list_of_integers[mid] <
                list_of_integers[mid + 1]):
            if int(size / 2) == 0:
                size = 2
            mid = mid + int(size / 2)
        else:
            return list_of_integers[mid]

