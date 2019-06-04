#  给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#  示例:
#  输入: n = 4, k = 2
#  输出:
#  [
  #  [2,4],
  #  [3,4],
  #  [2,3],
  #  [1,2],
  #  [1,3],
  #  [1,4],
#  ]

#  回溯法
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0 or n < k:
            return []
        out = []
        def helper(i, tmp):
            if i > n+1:
                return
            if len(tmp) == k:
                out.append(tmp)
                return
            for j in range(i, n+1):
                helper(j+1, tmp+[j])

        helper(1, [])
        return out
