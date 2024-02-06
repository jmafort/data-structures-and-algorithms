

def _quick_sort(array: list, start: int, end: int) -> None:
    if start >= end:
        return
    
    pivot_index = _partition(array, start, end)
    _quick_sort(array, start, pivot_index - 1)
    _quick_sort(array, pivot_index + 1, end)

def _partition(array: list, start: int, end: int) -> int:
    pivot = array[end]
    # Temporary pivot index
    i = start - 1

    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            _swap(array, i, j)

    i += 1
    _swap(array, i, end)

    return i

def _swap(array: list, i: int, j: int) -> None:
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def quick_sort(array: list) -> None:
    """
    Time complexity: worst case - O(n^2) | average case - O(n log n)
    Space complexity: O(log n)
    """
    _quick_sort(array, 0, len(array) - 1)

