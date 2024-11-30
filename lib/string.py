#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import Counter


def can_construct_string(str1: str, str2: str) -> bool:
    """
    Check if str1 can be constructed from characters in str2.
    Without Counter, go over str2 and construct a dictionary of characters and their counts.
    Then, go over str1 and decrement the count of the character in the dictionary.
    """
    st1, st2 = Counter(str1), Counter(str2)
    if st1 & st2 == st1:
        return True
    return False


def remove_non_numeric_chars(string):
    """
    Remove all non-numeric characters from a string.
    "sa 00sadl23.txt" -> "0023"
    """
    return re.sub(r'[^0-9]', '', string)


def remove_vowels(s):
    '''
    Remove all vowels from a string.
    '''
    return ''.join(filter(lambda x: x not in 'aeiouAEIOU', s))


def replace_chars_by_dict(s, replacement_dict):
    """
    Replace characters in a string by the values in the replacement_dict.
    """
    for k, v in replacement_dict.items():
        s = s.replace(k, v)
    return s


def roman_numeral_to_int(s: str) -> int:
    """
    Convert a roman numeral to an integer.
    """
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    pass_char = False
    for i, char in enumerate(s):
        if pass_char:
            pass_char = False
            continue
        char_val = roman_map[char]
        if i == len(s) - 1:
            char_next = None
        else:
            char_next = s[i + 1]
            char_next_val = roman_map[char_next]
        if char_next is None:
            total += char_val
        else:
            if char_next_val <= char_val:
                total += char_val
            else:
                total += char_next_val - char_val
                pass_char = True
    return total


def substrip(s, sub_s):
    """
    Strip trailing substring from a string.
    """
    sub_s_length = len(sub_s)
    if s.startswith(sub_s):
        s = s[sub_s_length:]
    if s.endswith(sub_s):
        s = s[:-sub_s_length]
    return s


def is_valid_parantheses(s):
    """
    Check if a string of parantheses is valid.
    """
    par_map = {')': '(', '}': '{', ']': '['}
    opens = par_map.values()
    stack = []
    for char in s:
        if char in opens:
            stack.append(char)
        else:
            if not stack or par_map[char] != stack[-1]:
                return False
            stack.pop()
    return not stack


if __name__ == '__main__':
    ## Test can_construct_string
    print()
    str1 = 'abc'
    str2 = 'aabbcc'
    print('Test can_construct_string with', str1, str2)
    print(can_construct_string(str1, str2))

    ## Test is_valid_parantheses
    print()
    print('Test is_valid_parantheses with "([])"')
    print(is_valid_parantheses('([])'))
    print('Test is_valid_parantheses with "([)]"')
    print(is_valid_parantheses('([)]'))

    ## Test remove_vowels
    print()
    print('Test remove_vowels with "sa 00sadl23.txt"')
    print(remove_vowels('sa 00sadl23.txt'))

    ## Test roman_numeral_to_int
    print()
    print('Test roman_numeral_to_int with "III (3)"')
    print(roman_numeral_to_int('III'))
    print('Test roman_numeral_to_int with "MDCCLXXIII (1773)"')
    print(roman_numeral_to_int('MDCCLXXIII'))
    print('Test roman_numeral_to_int with "MCMXCVI (1996)"')
    print(roman_numeral_to_int('MCMXCVI'))
