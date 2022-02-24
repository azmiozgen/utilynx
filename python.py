from collections import Counter
import json
import re

from tabulate import tabulate

def flatten_list_of_lists(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

def get_most_common_element_and_its_count(list_of_elements):
    '''
    Return the most common element and its count in a list.
    '''
    counter = Counter(list_of_elements)
    if not counter:
        return None, 0
    most_common, count = counter.most_common(1)[0]
    return most_common, count

def print_table(rows, headers=[], tablefmt='fancy_grid'):
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
    print(tabulate(rows, headers=headers, tablefmt=tablefmt))

def read_json(json_file):
    with open(json_file) as f:
        return json.load(f)

def remove_non_numeric_chars(string):
    '''
    Remove all non-numeric characters from a string.
    "sa 00sadl23.txt" -> "0023"
    '''
    return re.sub(r'[^0-9]', '', string)

def write_json(json_file, data, indent=4):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=indent)