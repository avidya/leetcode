#!/usr/bin/python
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# return 1->4->3->2->5->NULL.
#
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list. 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if not head or not head.next or m == n:
            return head
        count=0
        prev=None
        mark1=None
        mark2=None
        now=head
        while now:
            count+=1
            if count >= m and count <= n:
                if count == m:
                    mark1=prev
                    mark2=now
                    prev=now
                    now=now.next
                else: 
                    tmp=now.next
                    now.next=prev
                    if count == n:
                        if mark1:
                            mark1.next=now
                        else:
                            head=now
                        mark2.next=tmp
                        prev=mark2
                    else:
                        prev=now
                    now=tmp
            else:
                prev=now
                now=now.next
        return head
