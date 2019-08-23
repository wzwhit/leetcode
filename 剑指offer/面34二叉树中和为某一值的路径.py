# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        out = []

        def backtrack(root, tmp, summ):
            if summ == expectNumber and not root:
                if tmp not in out:
                    out.append(tmp)
                return
            if not root:
                return
            backtrack(root.left, tmp + [root.val], summ + root.val)
            backtrack(root.right, tmp + [root.val], summ + root.val)
            return

        backtrack(root, [], 0)
        return out