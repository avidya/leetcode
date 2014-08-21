#!/usr/bin/python

class Solution:
    def singleNumber(self, A):
        return reduce(lambda s, a: s^a, A)
