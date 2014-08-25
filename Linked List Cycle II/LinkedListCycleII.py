#!/usr/bin/python
#
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null. 
#
# Follow up:
# Can you solve it without using extra space? 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            print slow.val
            print fast.val
            if slow == fast:
                return slow
        return None
