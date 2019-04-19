# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#给定一个二叉树，返回其按层次遍历的节点值
#即逐层地，从左到右访问所有节点
#二叉树层次遍历
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        currentstack = [root]
        outlist = []
        while currentstack:
            res = []
            nextstack = []
            for node in currentstack:
                res.append(node.val)
                if node.left:
                    nextstack.append(node.left)
                if node.right:
                    nextstack.append(node.right)
            outlist.append(res)
            currentstack = nextstack
        return outlist
