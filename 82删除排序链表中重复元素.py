# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        p1 = head.next
        p2 = head
        s = ListNode(0)
        s.next = head
        out = s
        while p1:
            if p2.val != p1.val:
                p1 = p1.next
                s = p2
                p2 = p2.next
            else:
                while p2.val == p1.val:
                    if p1.next:
                        p1 = p1.next
                    else:
                        s.next = None
                        return out.next
                p2 = p1
                s.next = p1
                p1 = p1.next

        return out.next

