#!/usr/bin/python3

class Solution:
    #@return an integer
    def maxSubSum(self, l):
        m = l[0]
        if len(l) == 1:
            return m
        else:
            submax = 0
            for i in l:
                submax += i
                if submax > m:
                    m = submax
                if submax < 0:
                    submax = 0
        return m
        
