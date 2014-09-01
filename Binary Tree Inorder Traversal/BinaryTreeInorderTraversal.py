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
        nodes=[]
        results=[]
        nodes.append(root)
        while True:
            if len(nodes) == 0:
                return results
            node=nodes.pop()
            if node.right:
                nodes.append(node.right)
            if node.left:
                left=node.left
                node.left=None
                node.right=None
                nodes.append(node)
                nodes.append(left)
            else:
                results.append(node.val)
