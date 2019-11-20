#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/20/2019 1:52 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 112_Path_Sum.py.py
# Software:  PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        stack = []
        stack.append((root, sum - root.val))
        while len(stack)>0:
            node, curr_sum = stack.pop()
            if node.left is None and node.right is None and curr_sum == 0:
                return True
            if node.right is not None:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left is not None:
                stack.append((node.left, curr_sum - node.left.val))
        return False


