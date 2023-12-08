#!/usr/bin/python3
def multiply_by_2(my_dict):
    """print(multiply_by_2({"on": 5, "off": 7, "mi": 12}), end='**')"""
    return {key: val*2 for (key, val) in my_dict.items()}
