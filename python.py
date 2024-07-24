from collections import Counter
import json
import re

from tabulate import tabulate


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


def print_table(rows, headers=None, tablefmt='fancy_grid'):
    """
    Print a table with the given title and columns.
    rows: list of lists
    headers: list of strings
    tablefmt: str
    print_table([[1, 2, 3], [4, 5, 6]], headers=['a', 'b', 'c']) -->
    | a | b | c |
    |-----------|
    | 1 | 2 | 3 |
    |-----------|
    | 4 | 5 | 6 |
    |-----------|
    """
    if not headers:
        headers = []
    print(tabulate(rows, headers=headers, tablefmt=tablefmt))


def read_json(json_file):
    """
    Read a json file and return the data.
    """
    with open(json_file, encoding='utf-8') as f:
        return json.load(f)


def remove_non_numeric_chars(string):
    """
    Remove all non-numeric characters from a string.
    "sa 00sadl23.txt" -> "0023"
    """
    return re.sub(r'[^0-9]', '', string)


def remove_vowels(string):
    """
    Remove all vowels from a string.
    """
    return re.sub(r'[aeiouAEIOU]', '', string)
    # return ''.join(filter(lambda x: x not in 'aeiouAEIOU', string))


def write_json(json_file, data, indent=4):
    """
    Write data to a json file.
    """
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent)


if __name__ == '__main__':
    ## Test bubble_sort
    arr = [64, 34, 25, 12, 22, 11, 90]
    print('Test bubble_sort with', arr)
    print(bubble_sort(arr))

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

    ## Test print_table
    print()
    print('Test print_table with [[1, 2, 3], [4, 5, 6]]')
    print_table([[1, 2, 3], [4, 5, 6]])

    ## Test remove_vowels
    print()
    print('Test remove_vowels with "sa 00sadl23.txt"')
    print(remove_vowels('sa 00sadl23.txt'))
