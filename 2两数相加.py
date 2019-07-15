#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.56%)
# Total Accepted:    85.1K
# Total Submissions: 261.3K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        out = ListNode(0)
        p = out
        carry = 0
        while l1 and l2:
            out.next = ListNode(l1.val + l2.val + carry)
            if out.next.val > 9:
                out.next.val -= 10
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
            out = out.next
        while l1:
            out.next = ListNode(l1.val + carry)
            if out.next.val > 9:
                out.next.val -= 10
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            out = out.next
        while l2:
            out.next = ListNode(l2.val + carry)
            if out.next.val > 9:
                out.next.val -= 10
                carry = 1
            else:
                carry = 0
            l2 = l2.next
            out = out.next
        if carry == 1:
            out.next = ListNode(1)
        return p.next
