# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归,先序遍历
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

#  中序遍历
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def helper(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            if helper(left.left, right.right):
                if left.val != right.val:
                    return False
                return helper(left.right, right.left)
            else:
                return False
        return helper(root.left, root.right)
