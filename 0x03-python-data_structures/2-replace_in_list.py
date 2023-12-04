#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    @my_list: A python list
    @ix: Inx of th list
    @lmnt: Th lmnt to pop out
    """
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
