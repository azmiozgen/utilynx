from collections import Counter
import json
import re

from tabulate import tabulate

def flatten_list_of_lists(list_of_lists):
    '''
    Flatten a list of lists.
    [[1, 2], [3, 4]] -> [1, 2, 3, 4]
    '''
    return [item for sublist in list_of_lists for item in sublist]

def get_most_common_element_and_its_count(list_of_elements):
    '''
    Return the most common element and its count in a list.
    [1, 2, 3, 1, 2, 3, 1, 2, 3] -> (1, 3)
    '''
    counter = Counter(list_of_elements)
    if not counter:
        return None, 0
    most_common, count = counter.most_common(1)[0]
    return most_common, count

def print_table(rows, headers=None, tablefmt='fancy_grid'):
    '''
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
    '''
    if not headers:
        headers = []
    print(tabulate(rows, headers=headers, tablefmt=tablefmt))

def read_json(json_file):
    '''
    Read a json file and return the data.
    '''
    with open(json_file) as f:
        return json.load(f)

def remove_non_numeric_chars(string):
    '''
    Remove all non-numeric characters from a string.
    "sa 00sadl23.txt" -> "0023"
    '''
    return re.sub(r'[^0-9]', '', string)

def remove_vowels(string):
    '''
    Remove all vowels from a string.
    '''
    return re.sub(r'[aeiouAEIOU]', '', string)
    # return ''.join(filter(lambda x: x not in 'aeiouAEIOU', string))

def write_json(json_file, data, indent=4):
    '''
    Write data to a json file.
    '''
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=indent)


if __name__ == '__main__':
    ## Test flatten_list_of_lists
    print('Test flatten_list_of_lists with [[1, 2], [3, 4]]')
    print(flatten_list_of_lists([[1, 2], [3, 4]]))

    ## Test get_most_common_element_and_its_count
    print('Test get_most_common_element_and_its_count with [1, 2, 3, 1, 2, 3, 1, 2, 3]')
    print(get_most_common_element_and_its_count([1, 2, 3, 1, 2, 3, 1, 2, 3]))

    ## Test print_table
    print('Test print_table with [[1, 2, 3], [4, 5, 6]]')
    print_table([[1, 2, 3], [4, 5, 6]])

    ## Test remove_vowels
    print('Test remove_vowels with "sa 00sadl23.txt"')
    print(remove_vowels('sa 00sadl23.txt'))