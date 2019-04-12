# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#二叉树后序遍历迭代算法，先遍历左子树，再遍历右子树，再访问根节点
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        out = []
        lastnode = TreeNode(0)#记录上一节点
        while root != None or stack:
            while root != None:
                stack.append(root)
                root = root.left
            top = stack[-1]#栈顶节点
            #若上一节点是栈顶节点的右子树或者栈顶节点不存在右子树
            #访问栈顶节点，并出栈作为上一节点
            if lastnode == top.right or top.right == None:
                out.append(top.val)
                lastnode = stack.pop()
            #若栈顶节点有右子树且未访问，遍历右子树
            else:
                root = top.right
        return out
