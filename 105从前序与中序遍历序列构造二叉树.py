#  根据一棵树的前序遍历与中序遍历构造二叉树。
#  注意:
#  你可以假设树中没有重复的元素。
#  例如，给出
#  前序遍历 preorder = [3,9,20,15,7]
#  中序遍历 inorder = [9,3,15,20,7]
#  返回如下的二叉树：
    #  3
   #  / \
  #  9  20
    #  /  \
   #  15   7

#  前序第一个数是根节点，在中序中找到根节点，根节点前面是左子树，根节点右边是右子树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return root
