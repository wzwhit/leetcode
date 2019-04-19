# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.getchildtree(1, n)

    def getchildtree(self, s: int, e: int):
        out = []
        if s > e:
            return [None]
        for i in range(s, e+1):
            lefts = self.getchildtree(s, i-1)
            rights = self.getchildtree(i+1, e)
            for left in lefts:
                for right in rights:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    out.append(root)
        return out

