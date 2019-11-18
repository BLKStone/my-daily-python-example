#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/13/2019 5:39 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : Tree.py
# Software:  PyCharm

class BinaryTree:
    def __init__(self, data = None, left_child = None, right_child = None):
        self.val = data
        self.left = left_child
        self.right = right_child

    def __repr__(self):
        return "BinaryTree (%s)" % str(self.val)

    def __str__(self):
        return "BinaryTree (%s)" % str(self.val)

A = BinaryTree('A')
B = BinaryTree('B')
C = BinaryTree('C')
D = BinaryTree('D')
E = BinaryTree('E')
F = BinaryTree('F')
G = BinaryTree('G')
H = BinaryTree('H')
I = BinaryTree('I')

A.left = B
A.right = C

B.left = D
B.right = E

C.left = F
C.right = G

G.left = H
G.right = I