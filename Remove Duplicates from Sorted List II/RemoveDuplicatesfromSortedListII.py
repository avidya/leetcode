#!/usr/bin/python
#
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3. 
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
        prev=None
        now=head
        next_elem=now.next
        while True:
            if not next_elem:
                return head
            elif next_elem.val > now.val:
                if now.next == next_elem:
                    prev=now
                else:
                    if prev:
                        prev.next=next_elem
                    else:
                        head=next_elem
                now=next_elem
            else:
                if prev:
                    prev.next=None
                else:
                    head=None
            next_elem=next_elem.next
