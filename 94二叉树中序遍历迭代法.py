# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#二叉树中序遍历迭代法
#循环:根节点非空，根节点入栈，遍历左子树;
#     根节点为空，退栈作为根节点，访问根节点，遍历右子树
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        out = []
        while root != None or stack:
            if root != None:
                stack.append(root)#根节点非空，进栈
                root = root.left#遍历左子树
            else:
                root = stack.pop()#根节点为空，退栈作为根节点
                out.append(root.val)#访问根节点
                root = root.right#遍历右子树
        return out
