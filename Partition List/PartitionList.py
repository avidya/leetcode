#!/usr/bin/python
#
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5. 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if not head:
            return head
        now=head
        prev=None
        last=None
        while now:
            if now.val < x:
                if last == prev:
                    last=now
                    prev=now
                else:
                    # when into this branch, prev cannot be None 
                    prev.next=now.next
                    if last:
                        now.next=last.next
                        last.next=now
                        last=last.next
                    else:
                        now.next=head
                        head=now
                        last=now
                now=prev.next
            else:
                prev=now
                now=now.next
        return head
