#!/usr/bin/python
#
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#How many possible unique paths are there?

class Solution:
    #@return an integer
    def uniquePaths(self, m, n):
        from math import factorial as fact
        return fact(m+n-2)/(fact(m-1)*fact(n-1))

