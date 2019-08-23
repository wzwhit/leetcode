# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        p1 = pHead
        p2 = pHead
        length = 0
        while p1 and p2 and p1.next and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                p2 = pHead
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None