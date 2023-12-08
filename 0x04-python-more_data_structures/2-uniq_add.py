#!/usr/bin/python3
def uniq_add(arg: list):
    """Adds unique items in a list

    Args:
        arg (list): the list with a bunch of duplicates

        @example:
        ```py
        print(uniq_add([1,1,2,3,3,3,6])) -> 12
        ```

    Returns:
        int: The sum of all the unique items in the list.
    """
    return sum(set(arg))
