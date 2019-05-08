# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#二叉树后序遍历递归
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        out = []
        if root != None:
            return self.postorder(root, out)
        else: return out

    def postorder(self, root:TreeNode, out:List):
        if root != None:
            self.postorder(root.left, out)
            self.postorder(root.right, out)
            out.append(root.val)
        return out
