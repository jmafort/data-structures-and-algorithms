from typing import Any


def linear_search(generic_list: list, element: Any) -> int | None:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    for i in range(len(generic_list)):
        if generic_list[i] == element:
            return i
        
    return None
