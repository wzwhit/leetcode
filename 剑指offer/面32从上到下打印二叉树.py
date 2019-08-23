# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        curline = [root]
        out = []
        while curline:
            nextline = []
            for i in curline:
                if i:
                    out.append(i.val)
                    nextline.append(i.left)
                    nextline.append(i.right)
            curline = nextline[:]
        return out
