#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/18/2019 8:13 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 108_Convert_Sorted_Array_to_Binary_Search_Tree.py.py
# Software:  PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        # 初始条件
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        tn = self.makeBalencedBinarySearchTree(nums, 0, len(nums)-1)
        return tn

    def makeBalencedBinarySearchTree(self, nums, start, end):
        mid  = int((start + end ) / 2)
        tn = TreeNode(nums[mid])
        if mid > start:
            tn.left = self.makeBalencedBinarySearchTree(nums, start, mid - 1)
        if mid < end:
            tn.right = self.makeBalencedBinarySearchTree(nums, mid + 1, end)

        return tn

