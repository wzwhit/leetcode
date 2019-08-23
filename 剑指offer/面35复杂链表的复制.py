# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        hashtable = {}
        p = RandomListNode(0)
        pp = p
        head = pHead
        while head:
            p.next = RandomListNode(head.label)
            p = p.next
            hashtable[head] = p
            head = head.next
        head = pHead
        p = pp.next
        while head:
            p.random = hashtable.get(head.random)
            head = head.next
            p = p.next
        return pp.next
