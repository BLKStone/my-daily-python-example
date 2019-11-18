#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/18/2019 6:01 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 101_Symmetric_Tree.py.py
# Software:  PyCharm


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/symmetric-tree/
# 递归解法
# 两个左右子树互为镜像
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        return self.isMirror(root.left, root.right)



    def isMirror(self, t1, t2):
        """
        :param left:  TreeNode
        :param right: TreeNode
        :return: bool
        """
        if t1 is None and t2 is None:
            return True

        if t1 is None and t2 is not None:
            return False
        if t1 is not None and t2 is None:
            return False

        if t1.val != t2.val:
            return False

        final_flag = self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
        return final_flag
