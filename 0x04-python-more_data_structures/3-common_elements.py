#!/usr/bin/python3
def common_elements(set_1: set, set_2: set) -> set:
    """Returns an intersection set

    Args:
        set_1 (set): first set instance
        set_2 (set): You already saw the first one.

    Returns:
        set: Return a new set with overlapping values

        @example:
        ```py
        print(common_elements({2,3,4}, {3,2,5,4})) -> {2,3,4}
        ```
    """
    return set_1 & set_2
