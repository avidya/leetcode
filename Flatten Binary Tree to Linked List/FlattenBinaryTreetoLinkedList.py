#!/usr/bin/python
# 
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example,
# Given
# 
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# 
# The flattened tree should look like:
# 
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        node=root
        nodes=[]
        lastnode=None
        while node or nodes:
            if node:
                lastnode=node
                if node.right:
                    nodes.append(node.right)
                if node.left:
                    node.right=node.left
                    node.left=None
                    node=node.right
                else:
                    node=None
            else:
                node=nodes.pop()
                lastnode.right=node
