#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/20/2019 2:28 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : Breadth_First_Search.py
# Software:  PyCharm

import Tree
from collections import deque

def breadth_first_search(tree_node):

    queue = deque([])
    queue.append(tree_node)

    while len(queue) > 0:
        node = queue.popleft()

        if node is None:
            continue

        print(node.val)
        if node.left is None and node.right is None:
            continue

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


if __name__ == '__main__':
    a_tree = Tree.A
    breadth_first_search(a_tree)