# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or k == 0:
            return head
        p1 = p2 = head
        n = 1
        while p1.next != None:
            n += 1
            p1 = p1.next
        #print(n)
        #print(p1.val)
        k = k % n
        p1.next = head
        p1 = p1.next
        #print(p1.val)
        for i in range(0,k):
            p1 = p1.next
            #print(p1.val)
        for i in range(0,n-k-1):
            p1 = p1.next
            p2 = p2.next
        #print(p1.val,p2.val)
        p1.next = head
        s = p2.next
        p2.next = None
        return s
