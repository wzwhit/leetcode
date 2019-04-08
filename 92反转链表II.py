# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None or m == n:
            return head
        s = ListNode(0)
        s.next = head
        out = s#输出
        p = head#遍历链表的指针节点
        for i in range(n):
            if i < m-1:
                s = s.next#s为第m-1个节点
                p = p.next
            elif i == m-1:
                start = end = p#start为现链表的第m个节点，end为已反转部分链表的最后一个节点,即end一直为原链表的第m个节点
                p = p.next
                #print("s",start.val)
            else:
                #print(p.val)
                #p在m到n内向后遍历，把p移动到第m个节点的位置
                z = p.next
                p.next = start
                s.next = p
                end.next = z
                start = s.next
                p = z
                #print(s.val,start.val,end.val,p.val)
        return out.next
