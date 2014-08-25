#!/usr/bin/python
#
# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#   Given linked list: 1->2->3->4->5, and n = 2.
#   After removing the second node from the end, the linked list becomes 1->2->3->5.
#
# Note:
# Given n will always be valid.
# Try to do this in one pass. 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        count=n
        p1=head
        p2=None
        while count > 0:
            count-=1
            p1=p1.next
        while p1:
            p1=p1.next
            if p2:
                p2=p2.next
            else:
                p2=head
        if p2:
            p2.next=p2.next.next
            return head
        else:
            return head.next
