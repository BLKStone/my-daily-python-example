#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 11/13/2019 5:48 PM
# Author  : BLKStone
# Site    : http://wp.blkstone.me
# File    : Traversals.py.py
# Software:  PyCharm

import Tree

# 前序遍历
def pre_order_traversal(tree_node, stack):
    """
    :param tree_node: Tree.BinaryTree
    :param stack: list
    :return: list
    """
    if tree_node is not None:
        stack.append(tree_node)
        pre_order_traversal(tree_node.left, stack)
        pre_order_traversal(tree_node.right, stack)
        return stack

# 中序遍历
def in_order_traversal(tree_node, stack):
    """
    :param tree_node: Tree.BinaryTree
    :param stack: list
    :return: list
    """
    if tree_node is not None:
        in_order_traversal(tree_node.left, stack)
        stack.append(tree_node)
        in_order_traversal(tree_node.right, stack)
        return stack

# 后序遍历
def post_order_traversal(tree_node, stack):
    """
    :param tree_node: Tree.BinaryTree
    :param stack: list
    :return: list
    """
    if tree_node is not None:
        post_order_traversal(tree_node.left, stack)
        post_order_traversal(tree_node.right, stack)
        stack.append(tree_node)
        return stack


if __name__ == '__main__':
    a_tree = Tree.A
    stack = []
    pre_order_traversal(a_tree, stack)
    print(stack)
    stack = []
    in_order_traversal(a_tree, stack)
    print(stack)
    stack = []
    post_order_traversal(a_tree, stack)
    print(stack)
