#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/13/2019 3:43 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : main.py
# Software:  PyCharm

import random

class Solution(object):

    # Ordinary Solution
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Simple hack
        # Negative number will NEVER be a Palindrome.
        if x < 0:
            return False

        # Main logic
        number_str = str(x)
        number_length = len(number_str)
        end = int(number_length / 2) + 1
        flag = True
        for i in range(end):
            if number_str[i] == number_str[number_length - 1 - i]:
                continue
            else:
                flag = False
                break
        return flag

    # Mathematical Solution
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        div = 1

    def maxDivison(self, x):
        """
        :param x: int
        :return: int
        """
        div = 1
        while x >= 10:
            x = int(x / 10)
            div = div * 10
        return div

    def reverseNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_div = self.maxDivison(x)
        print(x)
        print(int(x/max_div))


if __name__ == '__main__':
    sol = Solution()


    for i in range(20):
        x = random.randint(1, 100000)
        sol.reverseNumber(x)





