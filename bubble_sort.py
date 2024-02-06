

def bubble_sort(array: list) -> None:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """

    n = len(array)

    for i in range(n):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                aux = array[j+1]
                array[j+1] = array[j]
                array[j] = aux

