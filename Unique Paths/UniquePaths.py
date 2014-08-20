#!/usr/bin/python
#
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#How many possible unique paths are there?

class Solution:
    #@return an integer
    def uniquePaths(self, m, n):
        step=m+n-2
        def recursiveSearch(_m, _n):
            '''
                inefficient recursive way : same node maybe counted multiple time.
            '''
            if _m < m and _n < n:
                return recursiveSearch(_m+1, _n) + recursiveSearch(_m, _n+1)
            elif _m == m and _n < n:
                return recursiveSearch(_m, _n+1)
            elif _m < m and _n == n:
                return recursiveSearch(_m+1, _n)
            else:
                return 1
    
        def dpSearch(_m, _n):
            '''
                Dynamic Programming way
            '''
            step_matrix=[[0 for x in xrange(_n)] for x in xrange(_m)]
            for i in xrange(_m):
                step_matrix[i][0]=1
            for i in xrange(_n):
                step_matrix[0][i]=1

            for i in xrange(1, _m):
                for j in xrange(1, _n):
                    step_matrix[i][j] = step_matrix[i-1][j] + step_matrix[i][j-1]

            return step_matrix[_m-1][_n-1]

#        return recursiveSearch(1, 1);
        return dpSearch(m, n)

solver = Solution()
print solver.uniquePaths(4, 3)
