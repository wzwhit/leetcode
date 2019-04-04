# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        p = head
        s = e = h = ListNode(0)
        if head.next == None:
            return head
        else:
            h.next = head.next
        while p.next != None:
            s = p.next.next
            p.next.next = p
            e.next = p.next
            p.next = s
            e = p
            p = p.next
            #print(p.val)
            if p == None:
                return h.next
        return h.next
