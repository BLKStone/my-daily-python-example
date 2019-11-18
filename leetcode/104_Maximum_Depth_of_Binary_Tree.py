#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/13/2019 4:16 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 104_Maximum_Depth_of_Binary_Tree.py
# Software:  PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None:
            return self.maxDepth(root.right) + 1
        if root.right is None:
            return self.maxDepth(root.left) + 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

