#!/usr/bin/python
# 
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
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
    def isBalanced(self, root):
        if not root:
            return True
        node=root
        lastnode=None
        nodes=[]
        heights=[]
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
                    if not node.right and not node.left:
                        heights.append(len(nodes))
                    elif not node.right or not node.left:
                        subtree=heights.pop()
                        if subtree-len(nodes) > 1:
                            return False
                        else:
                            heights.append(subtree)
                    else:
                        right=heights.pop()
                        left=heights.pop()
                        if abs(left - right) > 1:
                            return False
                        else:
                            heights.append(max(left,right))
                    lastnode=node
                    node=None
        return True
