#  反转一个单链表。
#  示例:
#  输入: 1->2->3->4->5->NULL
#  输出: 5->4->3->2->1->NULL
#  进阶:
#  你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

#  迭代
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p = ListNode(0)
        p.next = head
        p1 = head.next
        p2 = head
        while p1:
            p2.next = p1.next
            p1.next = p.next
            p.next = p1
            p1= p2.next
        return p.next

#  递归
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
