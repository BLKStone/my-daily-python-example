#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/22/2019 11:29 AM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 125_Valid_Palindrome.py.py
# Software:  PyCharm


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        valid_string = ""
        s = s.lower()

        for i in s:
            if '0' <= i <= '9':
                valid_string += i
            if 'a' <= i <= 'z':
                valid_string += i

        return self.determinePalindrome(valid_string)


    def determinePalindrome(self, valid_string):

        length = len(valid_string)
        if length == 0:
            return True

        mid = int(length / 2)

        final_flag = True
        for i in range(mid+1):
            if valid_string[i] != valid_string[length-1-i]:
                final_flag = False
                break
        return final_flag

