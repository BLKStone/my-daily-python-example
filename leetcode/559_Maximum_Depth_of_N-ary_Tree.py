#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/13/2019 4:41 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 559_Maximum_Depth_of_N-ary_Tree.py
# Software:  PyCharm



"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        elif len(root.children) == 0:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1
