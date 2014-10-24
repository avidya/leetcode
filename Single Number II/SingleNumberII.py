#!/usr/bin/python
#
# Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 

class Solution:

    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones=twos=0
        for i in A:
            ones=(ones^i)&(~twos)
            twos=(twos^i)&(~ones)
        return ones
