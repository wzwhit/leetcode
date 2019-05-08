# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#二叉树中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        out = []
        if root != None:
            return self.inorder(root, out)
        else: return out

    def inorder(self, root: TreeNode, out: List):
        if root != None:
            self.inorder(root.left,out)#遍历左子树
            out.append(root.val)#访问根节点
            self.inorder(root.right,out)#遍历右子树
        return out
