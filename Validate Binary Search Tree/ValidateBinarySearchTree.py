#!/usr/bin/python
# 
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
#   The left subtree of a node contains only nodes with keys less than the node's key.
#   The right subtree of a node contains only nodes with keys greater than the node's key.
#   Both the left and right subtrees must also be binary search trees.
# 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if not root:
            return True
        node=root
        nodes=[]
        vals=[]
        while node or nodes:
            if node:
                nodes.append(node)
                node=node.left
            else:    
                node=nodes.pop()
                vals.append(node.val)
                node=node.right
        for i in range(len(vals) - 1):
            if vals[i+1] <= vals[i]:
                return False
        return True
