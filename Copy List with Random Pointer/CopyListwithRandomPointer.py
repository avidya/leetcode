#!/usr/bin/python
#
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list. 
#
# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:

    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None;
        old=head
        new=None
        new_head=None
        d={} #{RandomListNode: (RandomListNode, Boolean)}

        def deepCopy(old_ptr, new_ptr, record):
            record[old_ptr]=(new_ptr, True)
            if not old_ptr.random:
                new_ptr.random=None
                return
            elif record.has_key(old_ptr.random):
                new_ptr.random=record[old_ptr.random][0]
                if record[old_ptr.random][1]:
                    return
                else:
                    deepCopy(old_ptr.random, new_ptr.random, record)
            else:
                new_ptr.random=RandomListNode(old_ptr.random.label)
                record[old_ptr.random]=(new_ptr.random, False)
                deepCopy(old_ptr.random, new_ptr.random, record)

        while old:
            tmp=None
            if d.has_key(old):
                tmp=d[old]
                new.next=tmp[0]
                new=new.next
                if not tmp[1]:
                    deepCopy(old, new, d)
            else:
                tmp=RandomListNode(old.label)
                if new:
                    new.next=tmp
                else:
                    new_head=tmp
                new=tmp
                d[old]=(new, False)
                deepCopy(old, new, d)
            old=old.next
        return new_head
