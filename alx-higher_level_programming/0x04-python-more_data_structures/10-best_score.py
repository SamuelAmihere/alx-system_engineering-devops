#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        temp = list(a_dictionary.items())
        temp.sort(key=lambda kv: kv[1], reverse=True)
        return temp[0][0]
    return None
