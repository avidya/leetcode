#!/usr/bin/python
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# 
# For example, this binary tree is symmetric:
# 
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 
# But the following is not:
# 
#     1
#    / \
#   2   2
#    \   \
#    3    3
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
    def isSymmetric(self, root):
        if not root:
            return True
        if (root.left == None) ^ (root.right == None):
            return False
        if (root.left == None) and (root.right == None):
            return True
        lnodes=[root.left]
        rnodes=[root.rigth]
        while lnodes:
            lnode=lnodes.pop()
            if not rnodes:
                return False
            else:
                rnode=rnodes.pop()
                if lnode.val != rnode.val:
                    return False
                if (lnode.left == None) ^ (rnode.right == None) or (lnode.right == None) ^ (rnode.left == None): 
                    return False
            if lnode.right:
                lnodes.append(lnode.right)
            if lnode.left:
                lnodes.append(lnode.left)
            if rnode.left:
                rnodes.append(rnode.left)
            if rnode.right:
                rnodes.append(rnode.right)
        return len(rnodes) == 0
