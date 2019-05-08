# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#层次遍历倒序输出
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        currentstack = [root]
        outlist = []
        out = []
        while currentstack:
            res = []
            nextstack = []
            for node in currentstack:#按行遍历
                res.append(node.val)
                if node.left:
                    nextstack.append(node.left)
                if node.right:
                    nextstack.append(node.right)
            currentstack = nextstack#用下一行替换当前行
            outlist.append(res)
        #n = len(outlist)
        #for i in range(len(outlist)-1, -1, -1):
            #out.append(outlist[i])

        return outlist[::-1]#从下往上倒序输出

