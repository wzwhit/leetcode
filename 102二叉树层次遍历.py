# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#给定一个二叉树，返回其按层次遍历的节点值
#即逐层地，从左到右访问所有节点
#二叉树层次遍历,迭代
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        currentstack = [root]#当前行
        outlist = []
        while currentstack:
            res = []
            nextstack = []#顺序保存当前行的所有左右子节点
            for node in currentstack:
                res.append(node.val)
                if node.left:
                    nextstack.append(node.left)
                if node.right:
                    nextstack.append(node.right)
            outlist.append(res)
            currentstack = nextstack#切换下一行
        return outlist
