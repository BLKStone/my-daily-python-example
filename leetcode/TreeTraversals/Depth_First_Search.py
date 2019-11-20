#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/20/2019 1:59 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : Depth_First_Search.py.py
# Software:  PyCharm

import Tree

def depth_first_search(tree_node):

    stack = []
    stack.append(tree_node)

    while len(stack) > 0:
        node = stack.pop()

        if node is None:
            continue

        print(node.val)
        if node.left is None and node.right is None:
            continue

        if node.left is not None:
            stack.append(node.left)

        if node.right is not None:
            stack.append(node.right)


if __name__ == '__main__':
    a_tree = Tree.A
    depth_first_search(a_tree)
