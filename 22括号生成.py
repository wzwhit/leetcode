#  给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#  例如，给出 n = 3，生成结果为：
#  [
  #  "((()))",
  #  "(()())",
  #  "(())()",
  #  "()(())",
  #  "()()()"
#  ]
#垃圾循环，在n-1上插入一个"()"
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        if n == 1:
            return ["()"]
        out = [["(",")"]]
        for i in range(n-1):
            out = self.InsertOneParenthesis(out)
        o = []
        for i in out:
            a = ''.join(i)
            o.append(a)
        return o

    def InsertOneParenthesis(self, out):
        o = []
        for i in range(len(out)):
            n = len(out[i])
            for j in range(n // 2):
                s = out[i].copy()
                s[j:j] = "("
                s[n+1-j:n+1-j] = ")"
                if s not in o:
                    o.append(s)
            for j in range(n // 2, n+1):
                s = out[i].copy()
                s[j:j] = "("
                s[j+1:j+1] = ")"
                if s not in o:
                    o.append(s)
        return o
