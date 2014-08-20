#!/usr/bin/python

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]:
            return 0
        if obstacleGrid[m-2][n-1] and obstacleGrid[m-1][n-2]:
            return 0
        
        step_matrix=[[0 for x in xrange(n)] for x in xrange(m)]    

        flag=False
        for i in xrange(m):
            if obstacleGrid[i][0]:
                flag=True
            step_matrix[i][0]=0 if flag else 1

        flag=False
        for i in xrange(n):
            if obstacleGrid[0][i]:
                flag=True
            step_matrix[0][i]=0 if flag else 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j]:
                    continue
                step_matrix[i][j] = step_matrix[i-1][j] + step_matrix[i][j-1]

        return step_matrix[m-1][n-1]

solution=Solution()
print solution.uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,0]])
