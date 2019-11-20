#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/19/2019 6:02 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : Selection_Sort.py.py
# Software:  PyCharm


def selection_sort(integers):
    """Search through a list of Integers using the selection sorting method.
    Search elements 0 through n - 1 and select smallest, swap with element at
    index 0, iteratively search through elements n - 1 and swap with smallest.
    """
    integers_clone = list(integers)

    for index in range(len(integers_clone) - 1, 0, -1):
        max_position = 0
        for location in range(1, index + 1):
            if integers_clone[location] > integers_clone[max_position]:
                max_position = location

        temp = integers_clone[index]
        integers_clone[index] = integers_clone[max_position]
        integers_clone[max_position] = temp

    return integers_clone


if __name__ == '__main__':
    integers = [1, 8, 23, 6, 2, 9, 4, 3, 7, 10, 86, 23]
    integers = selection_sort(integers)
    print(integers)
