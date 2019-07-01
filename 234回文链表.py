#  请判断一个链表是否为回文链表。
#  示例 1:
#  输入: 1->2
#  输出: false
#  示例 2:
#  输入: 1->2->2->1
#  输出: true
#  进阶：
#  你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#  先用快慢指针找到链表中间位置，反转后一半然后比较
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        p1 = p2 = head
        while p1 and p1.next:
            p2 = p2.next
            p1 = p1.next.next

        def reverseList(head):
            if not head or not head.next:
                return head
            p = reverseList(head.next)
            head.next.next = head
            head.next = None
            return p

        p = reverseList(p2)
        while head and p:
            if head.val != p.val:
                return False
            head = head.next
            p = p.next
        return True
