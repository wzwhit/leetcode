#  一条包含字母 A-Z 的消息通过以下方式进行了编码：
#  'A' -> 1
#  'B' -> 2
#  ...
#  'Z' -> 26
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。
#  示例 1:
#  输入: "12"
#  输出: 2
#  解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#  示例 2:
#  输入: "226"
#  输出: 3
#  解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

#  动态规划,考虑0的特殊情况
class Solution:
    def numDecodings(self, s: str) -> int:
        a = list(s)
        out = [0] * (len(a)+1)
        for i in range(0,len(a)):
            if i == 0:
                if a[0] == '0':
                    return 0
                out[i+1] = 1
            elif i == 1:
                if (int(a[i-1]+a[i]) > 26 and a[i] == '0') or a[i-1] == a[i] == '0':
                    return 0
                elif 0 < int(a[i-1]+a[i]) <= 26 and a[i] != '0':
                    out[i+1] = 2
                else:
                    out[i+1] = 1
            else:
                if (int(a[i-1]+a[i]) > 26 and a[i] == '0') or a[i-1] == a[i] == '0':
                    return 0
                elif 0 < int(a[i-1]+a[i]) <= 26 and a[i] != '0' and a[i-1] != '0':
                    out[i+1] = out[i] + out[i-1]
                elif 0 < int(a[i-1]+a[i]) <= 26 and a[i] == '0':
                    out[i+1] = out[i-1]
                else:
                    out[i+1] = out[i]
        return out[-1]
