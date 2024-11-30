#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np


def get_l2_norm(x, y):
    '''
    x: numpy array
    y: numpy array
    Calculate the l2 distance between two vectors
    '''
    return np.linalg.norm(x - y)


if __name__ == '__main__':
    ## Test get_l2_norm
    print('Test get_l2_norm with [[1, 2], [3, 4]] and [[5, 6], [7, 8]]')
    print(get_l2_norm(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])))
