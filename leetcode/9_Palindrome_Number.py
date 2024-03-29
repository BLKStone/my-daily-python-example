#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/11/2019 9:41 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 9_Palindrome_Number.py.py
# Software:  PyCharm

# https://leetcode-cn.com/problems/palindrome-number/
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

    def digitNumbers(self, x):
        """
        :param x: int
        :return: int
        """
        div = 1
        while x >= 10:
            x = int(x / div)
            div = div * 10
        return div

    def reverseNumber(self, x):
        """
        :type x: int
        :rtype: int
        """

        print(self.digitNumbers(529))






