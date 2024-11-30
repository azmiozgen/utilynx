#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_sqrt_from_scratch(x: int) -> int:
    """
    Get the square root of a number without using the sqrt function.
    Use binary search to find the square root.
    """
    if x == 0:
        return 0
    if x in [1, 2, 3]:
        return 1
    if x == 4:
        return 2
    upper = x // 2 + 1  ## Upper bound trick
    lower = 2
    while lower <= upper:
        root = lower + (upper - lower) // 2
        if root == x // root:
            return root
        if root > x // root:
            upper = root - 1
        else:
            lower = root + 1
    return upper


def get_digits(n):
    """
    Get the digits of a number.
    123 -> [1, 2, 3]
    """
    digits = []
    if n < 10:
        return [n]
    while n >= 10:
        digits.append(n % 10)
        n = n // 10
    digits.append(n)
    return digits[::-1]


if __name__ == '__main__':
    ## Test get_digits
    print()
    n = 123
    print('Test get_digits with', n)
    print(get_digits(n))

    ## Test get_sqrt_from_scratch
    print()
    print('Test get_sqrt_from_scratch with', 8)
    print(get_sqrt_from_scratch(8))
    print('Test get_sqrt_from_scratch with', 122)
    print(get_sqrt_from_scratch(122))