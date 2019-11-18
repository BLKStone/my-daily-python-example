#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/13/2019 5:38 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 783_Minimum_Distance_Between_BST_Nodes.py.py
# Software:  PyCharm




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 二叉搜索树的中序遍历是升序数组
# 遍历数组以求得最短距离

# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        self.in_order_traversal(root, stack)

        min_val = float('inf')
        for i in range(0, len(stack) - 1):
            diff = abs(stack[i] - stack[i + 1])
            min_val = min(min_val, diff)

        return min_val

    def in_order_traversal(self, tree_node, stack):

        if tree_node.left is not None:
            self.in_order_traversal(tree_node.left, stack)

        if tree_node is not None:
            stack.append(tree_node.val)

        if tree_node.right is not None:
            self.in_order_traversal(tree_node.right, stack)
