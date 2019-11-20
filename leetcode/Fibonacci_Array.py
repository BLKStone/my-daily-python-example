#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/20/2019 1:39 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : Fibonacci_Array.py.py
# Software:  PyCharm



def fibonacci_array(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_array(n - 1) + fibonacci_array(n - 2)



if __name__ == "__main__":
    for i in range(10):
        print(fibonacci_array(i), end=" ")
    print("")

