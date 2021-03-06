#!/usr/bin/python
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#
#   1
#    \
#     2
#    /
#   3
#
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if not root:
            return []
        result=[]
        nodes=[root]
        while True:
            if len(nodes) == 0:
                return result
            node=nodes.pop()
            result.append(node.val)
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)
