# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        def helper(p1,p2):
            if not p1 and not p2:
                return True
            if not p1 or not p2:
                return False
            if p1.val == p2.val:
                return helper(p1.left, p2.right) and helper(p1.right,p2.left)
            return False
        return helper(pRoot,pRoot)