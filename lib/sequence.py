#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


def climb_stairs(n):
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    For each n, you can get there either climbing 1 step from n-1 or 2 steps from n-2.
    So, the number of ways to get to n is the sum of the number of ways to get to n-1 and n-2.
    This is the Fibonacci sequence. Solution is the nth Fibonacci number.
    """
    if n in (0, 1):
        return 1
    prev, curr = 1, 1
    for _ in range(2, n+1):
        prev, curr = curr, prev + curr
    return curr


def find_power_set(s):
    """
    Find the power set of a set.
    Time complexity: O(2^n)
    Space complexity: O(2^n)
    """
    n = len(s)
    power_set = []
    for i in range(1 << n):  # 2^n (shift 1 left n times)
        subset = [s[j] for j in range(n) if (i & (1 << j))] # Check if jth bit is set in i
        power_set.append(subset)

    return power_set


def find_power_set_simpler(s):
    """
    Find the power set of a set.
    For each element in the set, we can either include it or exclude it.
    For the set [1, 2, 3]:
        1. start with [[], [1]]
        2. don't add or add 2 to each: [[], [2], [1], [1, 2]]
        3. don't add or add 3 to each: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
        4. continue until all elements are processed
    """
    first = s[0]
    ss = [[], [first]]
    for num in s[1:]:
        new_subsets = []
        for subset in ss:
            new_subsets.append(subset[:])
            subset.append(num)
            new_subsets.append(subset[:])
        ss = new_subsets[:]

    return ss


def find_single_number(nums):
    """
    Find the single number in a list of numbers where every number appears twice except for one.
    [2, 2, 1] -> 1
    [4, 1, 2, 1, 2] -> 4
    XOR operation is commutative and associative,
        meaning that we can rearrange them so that two identical element sitting next to each other
        and xor-ing them result in 0.
    Example:
    1 xor 2 xor 3 xor 1 xor 2 xor 3 xor 4 = (1 xor 1) xor (2 xor 2) xor (3 xor 3) xor 4
    = 0 xor 0 xor 0 xor 4
    = 4
    """
    xor = 0
    for num in nums:
        xor ^= num

    return xor


def flatten_list_of_lists(list_of_lists):
    """
    Flatten a list of lists.
    [[1, 2], [3, 4]] -> [1, 2, 3, 4]
    """
    return [item for sublist in list_of_lists for item in sublist]


def get_most_common_element_and_its_count(list_of_elements):
    """
    Return the most common element and its count in a list.
    [1, 2, 3, 1, 2, 3, 1, 2, 3] -> (1, 3)
    """
    counter = Counter(list_of_elements)
    if not counter:
        return None, 0
    most_common, count = counter.most_common(1)[0]
    return most_common, count


def get_pascal_triangle_all(n) -> List[List[int]]:
    """
    Get the Pascal's triangle of size n.
    """
    def get_next_row(row):
        row_next = [1]
        for i in range(len(row) - 1):
            row_next.append(row[i] + row[i + 1])
        row_next.append(1)
        return row_next
    result = [[1]]
    for _ in range(1, n):
        row_next = get_next_row(result[-1])
        result.append(row_next)
    return result


def get_pascal_triangle_row(n) -> List[int]:
    """
    Get the row of Pascal's triangle using recursion.
    """
    def get_next_row(row):
        row_next = [1]
        for i in range(len(row) - 1):
            row_next.append(row[i] + row[i + 1])
        row_next.append(1)
        return row_next
    if n == 0:
        return [1]
    return get_next_row(get_pascal_triangle_row(n - 1))


if __name__ == '__main__':
    ## Test climb_stairs
    print()
    n = 4
    print('Test climb_stairs with', n)
    print(climb_stairs(n))

    ## Test find_power_set
    print()
    s = [1, 2, 3]
    print('Test find_power_set with', s)
    print(find_power_set(s))

    ## Test find_power_set_simpler
    print()
    print('Test find_power_set_simpler with', s)
    print(find_power_set_simpler(s))

    ## Test find_single_number
    print()
    print('Test find_single_number with [2, 2, 1]')
    print(find_single_number([2, 2, 1]))

    ## Test flatten_list_of_lists
    print()
    print('Test flatten_list_of_lists with [[1, 2], [3, 4]]')
    print(flatten_list_of_lists([[1, 2], [3, 4]]))

    ## Test get_most_common_element_and_its_count
    print()
    print('Test get_most_common_element_and_its_count with [1, 2, 3, 1, 2, 3, 1, 2, 3]')
    print(get_most_common_element_and_its_count([1, 2, 3, 1, 2, 3, 1, 2, 3]))

    ## Test get_pascal_triangle_all
    print()
    n = 3
    print('Test get_pascal_triangle_all with', n)
    print(get_pascal_triangle_all(n))

    ## Test get_pascal_triangle_row
    print()
    n = 3
    print('Test get_pascal_triangle_row with', n)
    print(get_pascal_triangle_row(n))
