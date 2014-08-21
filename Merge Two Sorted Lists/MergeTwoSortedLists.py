#!/usr/bin/python
#
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        head=None
        ptr=None
        h1=l1
        h2=l2
        while True:
            if h1.val <= h2.val:
                if head:
                    ptr.next=h1
                else:
                    head=h1
                ptr=h1
                h1=h1.next
                if not h1:
                    ptr.next=h2
                    return head
            else:
                if head:
                    ptr.next=h2
                else:
                    head=h2
                ptr=h2
                h2=h2.next
                if not h2:
                    ptr.next=h1
                    return head
