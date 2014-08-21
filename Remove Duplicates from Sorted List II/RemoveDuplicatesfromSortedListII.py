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
        now=head.next
        d={}
        while now:
            if d.has_key(now.val):
                if prev:
                    prev.next=now.next
                else:
                    head=now.next
            else:    
                p1=None
                p2=head
                flag=False
                while p2 != now:
                    if p2.val == now.val:
                        d[now.val]=1
                        if p2.next != now:
                            if p1:
                                p1.next=p2.next
                            else:
                                head=p2.next
                        else:
                            flag=True
                            if p1:
                                prev=p1
                                p1.next=now.next
                            else:
                                prev=None
                                head=now.next
                        break
                    else:
                        p1=p2
                        p2=p2.next
                if not flag:
                    prev=now
            now=now.next
        return head
