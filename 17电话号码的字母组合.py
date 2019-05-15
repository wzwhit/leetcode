#  给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#  "2":"abc",
#  "3":"def",
#  "4":"ghi",
#  "5":"jkl",
#  "6":"mno",
#  "7":"pqrs",
#  "8":"tuv",
#  "9":"wxyz"
#  示例:
#  输入："23"
#  输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

#  组合的循环次数不一定，所以用迭代
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        letter = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        s = []
        for i in digits:
            n = int(i) - 2
            a = [i for i in letter[n]]
            s.append(a)
        while len(s) > 1:
            s = self.Combination(s)
        return s[0]

    def Combination(self, s):
        o = []
        for i in s[0]:
            for j in s[1]:
                o.append(i + j)
        s[0:2] = [o]
        return s
