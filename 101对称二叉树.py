# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return self.isSameTree(root, root)
        else:
            return True

    def isSameTree(self, p:TreeNode, q:TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.left)
        else:
            return False
