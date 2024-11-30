#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bubble_sort(arr):
    """
    Bubble sort an array.
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap
    return arr


if __name__ == '__main__':
    ## Test bubble_sort
    arr = [64, 34, 25, 12, 22, 11, 90]
    print('Test bubble_sort with', arr)
    print(bubble_sort(arr))
