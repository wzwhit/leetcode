# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 迭代
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 and not pHead2:
            return None
        if not pHead1 or not pHead2:
            return pHead1 or pHead2
        p = ListNode(0)
        pp = p
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                p.next = ListNode(pHead1.val)
                pHead1 = pHead1.next
            else:
                p.next = ListNode(pHead2.val)
                pHead2 = pHead2.next
            p = p.next
        if not pHead1:
            while pHead2:
                p.next = ListNode(pHead2.val)
                p = p.next
                pHead2 = pHead2.next
        elif not pHead2:
            while pHead1:
                p.next = ListNode(pHead1.val)
                p = p.next
                pHead1 = pHead1.next
        return pp.next

# 递归
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 and not pHead2:
            return None
        if not pHead1 or not pHead2:
            return pHead1 or pHead2
        if pHead1.val <= pHead2.val:
            p = ListNode(pHead1.val)
            p.next = self.Merge(pHead1.next, pHead2)
        else:
            p = ListNode(pHead2.val)
            p.next = self.Merge(pHead1, pHead2.next)
        return p