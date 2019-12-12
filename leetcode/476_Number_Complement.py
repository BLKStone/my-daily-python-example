#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/22/2019 11:57 AM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 476_Number_Complement.py.py
# Software:  PyCharm

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        length = num.bit_length()

        xor_partners = 1
        for i in range(length-1):
            xor_partners = xor_partners << 1
            xor_partners = xor_partners + 1

        # print("{0:b}".format(xor_partners))

        return num ^ xor_partners


if __name__ == '__main__':
    sol = Solution()
    print(sol.findComplement(5))

