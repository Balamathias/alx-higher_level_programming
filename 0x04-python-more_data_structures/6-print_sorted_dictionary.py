#!/usr/bin/python3
def print_sorted_dictionary(my_dict: dict):
    """_summary_

    Args:
        my_dict (dict): _description_
    """
    for k in sorted(my_dict.keys()):
        print("{}: {}".format(k, my_dict[k]))
