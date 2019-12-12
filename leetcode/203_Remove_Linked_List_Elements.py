#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/22/2019 12:13 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 203_Remove_Linked_List_Elements.py.py
# Software:  PyCharm

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        dummy_node = ListNode(head.val)
        dummy_node.next = head

        prev = dummy_node

        while prev.next is not None:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next

        return dummy_node.next





