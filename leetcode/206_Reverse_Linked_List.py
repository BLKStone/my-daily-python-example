#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/22/2019 1:14 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : 206_Reverse_Linked_List.py
# Software:  PyCharm


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head

        prev = None
        curr = head
        while curr is not None:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        return prev


if __name__ == '__main__':
    pass