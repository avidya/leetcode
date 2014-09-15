#!/usr/bin/python
# 
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
# 
# For example,
# Given n = 3, there are a total of 5 unique BST's.
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# 

class Solution:

    # @return an integer
    def numTrees(self, n):
        f1=1
        f2=2
        if n == 1:
            return f1
        elif n == 2:
            return f2
        else:
            record=[f1, f2]
            for i in range(2,n):
                fn=2*record[-1]
                for j in range(1,i):
                    fn+=record[j-1]*record[i-j-1]
                record.append(fn)
            fn=record[-1]
            return fn
