#  给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#  示例 1:
#  输入: num1 = "2", num2 = "3"
#  输出: "6"
#  示例 2:
#  输入: num1 = "123", num2 = "456"
#  输出: "56088"
#  说明：
    #  num1 和 num2 的长度小于110。
    #  num1 和 num2 只包含数字 0-9。
    #  num1 和 num2 均不以零开头，除非是数字 0 本身。
    #  不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

#  num1的第i位(高位从0开始)和num2的第j位相乘的结果在乘积中的位置是[i+j, i+j+1]
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        out = [0 for i in range(n1+n2)]
        for i in range(n1):
            for j in range(n2):
                s = int(num1[i]) * int(num2[j])
                out[i+j] += s // 10
                out[i+j+1] += s % 10
        while out[0] == 0 and len(out) > 1:
            out = out[1:]
        for i in range(len(out)-1, 0, -1):
            if out[i] > 9:
                out[i-1] += out[i] // 10
                out[i] = out[i] % 10
        o = [str(i) for i in out]
        o = ''.join(o)
        return o
