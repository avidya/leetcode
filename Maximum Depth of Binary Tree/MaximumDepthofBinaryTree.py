#!/usr/bin/python
#
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        def recursiveVisit(node, depth):
            return max(recursiveVisit(node.left, depth+1), recursiveVisit(node.right, depth+1)) if node else depth
        return recursiveVisit(root, 0)
