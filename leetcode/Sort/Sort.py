#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/19/2019 6:07 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : Sort.py.py
# Software:  PyCharm


def bubble_sort(integers):
    integers_clone = list(integers)
    for index in range(len(integers_clone)-1, 0, -1):
        for location in range(index):
            if integers_clone[location] > integers_clone[location+1]:
                temp = integers_clone[location]
                integers_clone[location] = integers_clone[location+1]
                integers_clone[location+1] = temp

    return integers_clone

def selection_sort(integers):
    integers_clone = list(integers)

    for index in range(len(integers_clone)-1, 0, -1):
        max_position = 0
        for location in range(1, index+1):
            if integers_clone[location] > integers_clone[max_position]:
                max_position = location

        temp = integers_clone[index]
        integers_clone[index] = integers_clone[max_position]
        integers_clone[max_position] = temp

    return integers_clone



if __name__ == '__main__':
    integers = [1, 8, 23, 6, 2, 9, 4, 3, 7, 10, 86, 23]
    integers = bubble_sort(integers)
    integers_clone = selection_sort(integers)
    print(integers)
    print(integers_clone)

