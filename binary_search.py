from typing import Any


def binary_search(ordered_list: list, element: Any) -> int | None:
    """
    Time complexity: O(log n)
    Space complexity: O(1)
    """

    left: int = 0
    right: int = len(ordered_list) - 1
    
    while(left <= right):
        middle: int = (left + right) // 2

        if ordered_list[middle] == element:
            return middle
        elif ordered_list[middle] < element:
            left = middle + 1
        else:
            right = middle - 1

    return None

