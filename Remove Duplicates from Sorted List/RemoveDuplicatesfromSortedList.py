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
        now=head
        next_elem=now.next
        while True:
            if not next_elem:
                return head
            elif next_elem.val > now.val:
                now.next=next_elem
                now=next_elem
                next_elem=now.next
            else:
                next_elem=next_elem.next
                now.next=None
