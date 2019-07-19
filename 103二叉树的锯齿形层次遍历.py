#  给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#  例如：
#  给定二叉树 [3,9,20,null,null,15,7],
    #  3
   #  / \
  #  9  20
    #  /  \
   #  15   7
#  返回锯齿形层次遍历如下：
#  [
  #  [3],
  #  [20,9],
  #  [15,7]
#  ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#  与层次遍历一样，加一个标志位来改变每行遍历的方向
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        current = [root]
        out = []
        line = 0
        while current:
            line = 1 - line
            # print(out)
            nextline = []
            o = []
            for i in current:
                if i:
                    if line == 1:
                        nextline.append(i.left)
                        nextline.append(i.right)
                    else:
                        nextline.append(i.right)
                        nextline.append(i.left)
                    o.append(i.val)
            if o != []:
                out.append(o)
            current = nextline[::-1]
        return out

