#!/usr/bin/python3
def only_diff_elements(a: set, b: set) -> set:
    """Returns the only difference in two sets

    Args:
        a (set): _description_
        b (set): _description_

    Returns:
        set: _description_

        @example:
        ```py
        print(only_diff_elements({2,3}, {1,3}))
        ```
    """
    return a ^ b
