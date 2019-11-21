#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/20/2019 4:09 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : Long_Integer_Add.py.py
# Software:  PyCharm

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return self.add_sum(num1, num2)

    def add_sum(self, integer_a, integer_b):
        a_len = len(integer_a)
        b_len = len(integer_b)

        if a_len <= b_len:
            short_integer = "" + integer_a
            long_integer = "" + integer_b
            long_length = len(long_integer)
            short_length = len(short_integer)
        else:
            short_integer = "" + integer_b
            long_integer = "" + integer_a
            long_length = len(long_integer)
            short_length = len(short_integer)

        integer_sum = list(long_integer)

        diff = long_length - short_length
        flag = False

        for i in range(short_length - 1, -1, -1):
            bit_a = short_integer[i]
            bit_b = long_integer[i + diff]
            if flag:
                flag, _bit_sum = self.bit_sum(str(int(bit_a) + 1), bit_b)
            else:
                flag, _bit_sum = self.bit_sum(bit_a, bit_b)
            integer_sum[i + diff] = _bit_sum

        diff_idx = 1
        while flag:
            if diff - diff_idx < 0:
                temp = ["1"]
                temp.extend(integer_sum)
                integer_sum = temp
                break
            bit_b = long_integer[diff - diff_idx]
            flag, _bit_sum = self.bit_sum(bit_b, 1)
            integer_sum[diff - diff_idx] = _bit_sum
            diff_idx += 1
        return ''.join(integer_sum)


    def bit_sum(self, a, b):
        int_a = int(a)
        int_b = int(b)
        flag = False
        int_sum = int_a + int_b
        if int_sum >= 10:
            flag = True
            int_sum = int_sum - 10
        str_sum = str(int_sum)
        return flag, str_sum

if __name__ == "__main__":
    sol = Solution()
    res = sol.addStrings("999", "1")
    print(res)


