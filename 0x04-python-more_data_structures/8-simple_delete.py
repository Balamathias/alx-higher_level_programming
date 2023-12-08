#!/usr/bin/python3
def simple_delete(my_dict: dict, key="") -> dict:
    my_dict.pop(key, None)
    return my_dict
