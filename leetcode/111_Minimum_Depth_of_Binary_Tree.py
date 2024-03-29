#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/11/2019 9:51 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 111_Minimum_Depth_of_Binary_Tree.py.py
# Software:  PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
