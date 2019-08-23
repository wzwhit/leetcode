# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return pHead
        p1 = pHead
        p2 = pHead.next
        s = ListNode(0)
        s.next = p1 #指向p1
        out = s#输出
        while p1 and p2:
            if p1 and p2 and p1.val != p2.val:#不相等整体往后挪
                s = s.next
                p1 = p1.next
                p2 = p2.next
            else:
                while p2 and p1.val == p2.val:#相等，p2往后挪，找到所有相等的节点
                    p2 = p2.next
                p1 = p2 #p1和p2不等了，把p1挪到p2，p2后挪，s位置不动，指向p1
                if p2:
                    p2 = p2.next
                s.next = p1
        return out.next
