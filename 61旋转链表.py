# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or k == 0:
            return head
        p = head
        n = 1
        while p.next != None:
            n += 1
            p = p.next
        #print(n)
        e = p
        #print(e.val)
        p = head
        if n < 2 or k%n == 0:
            return head
        k = k % n
        for i in range(0,n-k-1):
            p = p.next
        s = p.next
        p.next = None
        e.next = head
        head = s
        return head
