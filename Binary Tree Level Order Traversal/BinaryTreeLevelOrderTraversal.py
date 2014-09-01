#!/usr/bin/python
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
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
# return its level order traversal as:
# 
# [
#   [3],
#   [9,20],
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
    def levelOrder(self, root):
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
            result.append(t)
        return result
