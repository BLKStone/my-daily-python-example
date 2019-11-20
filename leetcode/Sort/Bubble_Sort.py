#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/19/2019 5:52 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : Bubble_Sort.py.py
# Software:  PyCharm


def bubble_sort(integers):
    """
    Sort a list of integers using a simple bubble sorting method.
    Compare each element with its neighbor (except the last index)
    with its neighbor to the right, perform same check iteratively
    with the last n elements not being checked because they are sorted.
    """
    integers_clone = list(integers)

    for number in range(len(integers_clone) - 1, 0, -1):
        for i in range(number):
            if integers_clone[i] > integers_clone[i + 1]:
                temp = integers_clone[i]
                integers_clone[i] = integers_clone[i + 1]
                integers_clone[i + 1] = temp

    return integers_clone


if __name__ == '__main__':
    integers = [1, 8, 23, 6, 2, 9, 4, 3, 7, 10, 86, 23]
    integers = bubble_sort(integers)
    print(integers)
