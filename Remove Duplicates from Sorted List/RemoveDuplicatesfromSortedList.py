#!/usr/bin/python
#
# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3. 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        prev=head
        now=head.next
        d={head.val:1}
        while now:
            if d.has_key(now.val):
                prev.next=None
                now=now.next
            else:
                d[now.val]=1
                prev.next=now
                prev=now
                now=now.next
        return head
