#!/usr/bin/python

class Solution:
    def singleNumber(self, A):
        for i in A[1:]:
            A[0]=A[0] ^ i
        return A[0]

solution=Solution()
print solution.singleNumber([3, 5, 6, 4, 5, 6, 3])
