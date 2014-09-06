#!/usr/bin/python
# 
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        depth=1
        now=[]
        n=[root]
        while n:
            now=n
            n=[]
            for i in now:
                if not i.left and not i.right:
                    return depth
                if i.left:
                    n.append(i.left)
                if i.right:
                    n.append(i.right)
            depth+=1
