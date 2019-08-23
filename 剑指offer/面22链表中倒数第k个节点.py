# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return None
        p = head
        length = 0
        while p:
            p = p.next
            length += 1
        if k > length:
            return None
        if k == length:
            return head
        p = head
        p1 = head
        for _ in range(k):
            p1 = p1.next
        while p1 and p1.next:
            p1 = p1.next
            p = p.next
        return p.next