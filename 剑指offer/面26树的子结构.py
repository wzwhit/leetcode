# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSame(self, head1, head2):
        if not head2:
            return True
        if not head1 and head2:
            return False
        if head1.val == head2.val:
            return self.isSame(head1.left, head2.left) and self.isSame(head1.right, head2.right)
        else:
            return False

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        stack = []
        out = False
        while pRoot1 or stack:
            while pRoot1:
                if pRoot1.val == pRoot2.val:
                    out = out or self.isSame(pRoot1, pRoot2)
                stack.append(pRoot1)
                pRoot1 = pRoot1.left
            pRoot1 = stack.pop()
            pRoot1 = pRoot1.right

        return out

