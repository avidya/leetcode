# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None

        carry = 0
        r = ListNode(0)
        n = r
        n1 = l1
        n2 = l2
        
        while n1 or n2:
            n.next = ListNode(0)
            n = n.next
            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0
            v = v1 + v2 + carry
            x = v % 10
            carry = 1 if v > 9 else 0
            n.val = x
            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next
        if carry == 1:
            n.next = ListNode(1)
        return r.next
