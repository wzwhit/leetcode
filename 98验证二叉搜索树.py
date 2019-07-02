# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#  假设一个二叉搜索树具有如下特征：
    #  节点的左子树只包含小于当前节点的数。
    #  节点的右子树只包含大于当前节点的数。
    #  所有左子树和右子树自身必须也是二叉搜索树。
###中序遍历，保证中序遍历结果是升序为有效，否则为无效
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.val == None:
            return False
        stack = []
        out = []
        while root != None or stack:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            out.append(root.val)
            root = root.right
        for i in range(len(out)-1):
            if out[i] >= out[i+1]:
                return False
        return True
###
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        min = -2147483649
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= min:
                return False
            min = root.val
            root = root.right
        return True
#  递归
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        out = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            out.append(root.val)
            helper(root.right)
        helper(root)
        return out == sorted(out) and len(out) == len(set(out))
