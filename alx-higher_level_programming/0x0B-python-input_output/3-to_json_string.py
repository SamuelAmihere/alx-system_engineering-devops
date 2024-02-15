#!/usr/bin/python3
"""A module with to_json_string function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a
    string object
    """
    return (json.dumps(my_obj))
