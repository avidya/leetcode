#!/usr/bin/python
#
# Given a binary tree, return the inorder traversal of its nodes' values.
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
# return [1,3,2].
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
    def inorderTraversal(self, root):
        if not root:
            return []
        results=[]
        nodes=[]
        node=root
        while len(nodes) > 0 or node:
            if node:
                nodes.append(node)
                node=node.left
            else:
                node=nodes.pop()
                results.append(node.val)
                node=node.right
        return results
