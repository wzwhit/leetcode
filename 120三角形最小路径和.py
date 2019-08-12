#  给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#  例如，给定三角形：
#  [
     #  [2],
    #  [3,4],
   #  [6,5,7],
  #  [4,1,8,3]
#  ]
#  自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#  说明：
#  如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。


# dp
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        if not triangle[0]:
            return 0
        dp = [[triangle[i][j] for j in range(len(triangle[i]))] for i in range(len(triangle))]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] += dp[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] += dp[i - 1][j - 1]
                else:
                    dp[i][j] += min(dp[i-1][j], dp[i-1][j-1])

        return min(dp[-1][:])
