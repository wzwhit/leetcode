#  给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#  例如，给出 n = 3，生成结果为：
#  [
  #  "((()))",
  #  "(()())",
  #  "(())()",
  #  "()(())",
  #  "()()()"
#  ]

#回溯算法，递归添加'(',')',根据左右括号个数判断是否可以组成有效括号组合
#成功插入括号n-1，则左右括号个数都为0的时候为有效组合
#  n = 2,输出:
#  2 2
#  1 2 (
#  0 2 ((
#  -1 2 (((
#  0 1 (()
#  -1 1 (()(
#  0 0 (()) 有效
#  1 1 ()
#  0 1 ()(
#  -1 1 ()((
#  0 0 ()() 有效
#  1 0 ())
#  2 1 )
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(left_p, right_p, tmp):
            if left_p == 0 and right_p == 0:
                res.append(tmp)
                return
            if left_p < 0 or right_p < 0 or left_p > right_p:
                return
            helper(left_p-1, right_p, tmp+"(")
            helper(left_p, right_p-1, tmp+")")
        helper(n, n, "")
        return res
