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
        ring=False
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                ring=True
                break
        if not ring:
            return None
        else:
            slow=head
            while slow != fast:
                slow=slow.next
                fast=fast.next
            return slow
