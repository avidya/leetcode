#!/usr/bin/python
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# return [3,2,1].
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
    def postorderTraversal(self, root):
        results=[]
        node=root
        lastnode=None
        nodes=[]
        while len(nodes) > 0 or node:
            if node:
                nodes.append(node)
                node=node.left
            else:
                node=nodes.pop()
                if node.right and node.right != lastnode:
                    nodes.append(node)
                    node=node.right
                else:
                    results.append(node.val)
                    lastnode=node
                    node=None
        return results
