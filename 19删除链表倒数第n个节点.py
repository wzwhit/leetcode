# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or n == 0:
            return head
        p1 = p2 = head
        for _ in range(n):
            p1 = p1.next
        if p1 == None:
            return head.next
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        s = p2.next
        p2.next = s.next
        return head
