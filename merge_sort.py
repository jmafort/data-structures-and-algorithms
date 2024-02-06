

def merge(left: list, right: list) -> list:
    result = []
    
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right [0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while len(left) > 0:
        result.append(left[0])
        left = left[1:]

    while len(right) > 0:
        result.append(right[0])
        right = right[1:]

    return result

def merge_sort(array: list) -> list:
    """
    Time complexity: O(n log n)
    Space complexity: O(n)
    """

    if len(array) <= 1:
        return array

    left: list = array[:len(array)//2]
    right: list = array[len(array)//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

