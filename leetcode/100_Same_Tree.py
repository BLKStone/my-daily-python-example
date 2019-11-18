#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/18/2019 4:50 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 100_Same_Tree.py.py
# Software:  PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归解法

# https://leetcode-cn.com/problems/same-tree/
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        if p.val != q.val:
            return False

        final_flag = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return final_flag