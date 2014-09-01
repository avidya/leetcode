#!/usr/bin/python
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
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
# return its bottom-up level order traversal as:
# 
# [
#   [15,7],
#   [9,20],
#   [3]
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
    def levelOrderBottom(self, root):
        if not root:
            return []
        now=[]
        n=[root]
        result=[]
        while n:
            now=n
            n=[]
            t=[]
            for i in now:
                if i.left:
                    n.append(i.left)
                if i.right:    
                    n.append(i.right)
                t.append(i.val)
            result.insert(0, t)
        return result
