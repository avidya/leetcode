#!/usr/bin/python
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
# 
# For example:
# Given binary tree {3,9,20,#,#,15,7},
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# return its zigzag level order traversal as:
# 
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        now=[]
        n=[root]
        result=[]
        l2r=False
        while n:
            now=n
            n=[]
            t=[]
            for i in now:
                if i.left:
                    n.append(i.left)
                if i.right:
                    n.append(i.right)
                if l2r:
                    t.insert(0, i.val)
                else:
                    t.append(i.val)
            result.append(t)
            l2r=not l2r
        return result
