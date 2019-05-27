#  给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#  按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
    #  "123"
    #  "132"
    #  "213"
    #  "231"
    #  "312"
    #  "321"
#  给定 n 和 k，返回第 k 个排列。
#  说明：
    #  给定 n 的范围是 [1, 9]。
    #  给定 k 的范围是[1,  n!]。
#  示例 1:
#  输入: n = 3, k = 3
#  输出: "213"
#  示例 2:
#  输入: n = 4, k = 9
#  输出: "2314"

#  找规律
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def helper(lst, k, out):
            m = len(lst)
            if m <= 1 or k <= 1:
                out += ''.join([i for i in lst])
                return out
            s = math.factorial(m-1)
            i = k // s
            j = k % s
            if j == 0:
                i -= 1
                j = s
            out += lst[i]
            return helper(lst[:i]+lst[i+1:], j, out)
        lst = [str(i) for i in range(1,n+1)]
        return helper(lst, k, "")
