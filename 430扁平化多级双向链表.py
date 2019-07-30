#  您将获得一个双向链表，除了下一个和前一个指针之外，它还有一个子指针，可能指向单独的双向链表。这些子列表可能有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
#  扁平化列表，使所有结点出现在单级双链表中。您将获得列表第一级的头部。
#  示例:
#  输入:
 #  1---2---3---4---5---6--NULL
         #  |
         #  7---8---9---10--NULL
             #  |
             #  11--12--NULL
#  输出:
#  1-2-3-7-8-11-12-9-10-4-5-6-NULL


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def fun(node):
            # 一定要用global定义pre，保证在底层递归返回上层时保留底层
            # 最后一个节点，使其成为上层递归位置结束后第一个节点的前驱 if node:
            global pre
            pre=node
            if node.child:
                fun(node.child)
                next_node=node.next
                node.next=node.child
                node.child.prev=node
                node.child=None
                if next_node:
                    pre.next=next_node
                    next_node.prev=pre
            if node.next:
                fun(node.next)
        fun(head)
        return head

