

def insertion_sort(array: list) -> None:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """

    i = 1
    while i < len(array):
        curr_element = array[i]
        j = i
        while j > 0 and array[j-1] > curr_element:
            array[j] = array[j-1]
            j -= 1
        array[j] = curr_element
        i += 1
 
