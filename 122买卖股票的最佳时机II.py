#  给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#  设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#  示例 1:
#  输入: [7,1,5,3,6,4]
#  输出: 7
#  解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     #  随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#  示例 2:
#  输入: [1,2,3,4,5]
#  输出: 4
#  解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     #  注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     #  因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#  示例 3:
#  输入: [7,6,4,3,1]
#  输出: 0
#  解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = max = 0
        p = 0
        i = 0
        while i < len(prices):
            j = i + 1
            while j < len(prices) and prices[j-1] > prices[j]:
                j += 1
            min = j - 1
            while j < len(prices) and prices[j-1] < prices[j]:
                j += 1
            max = j-1

            p += prices[max] - prices[min]
            i = max + 1
        return p

#  动态规划
#  状态转移方程：
#  dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
#  dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
#  k为买卖次数，这里k不限制，所以可以省略不考虑
#  i为天数，0/1表示是否持有股票
#  考虑初始状态i=0时的情况
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N < 2:
            return 0
        O = [[0 for _ in range(2)] for _ in range(N)]
        for i in range(N):
            if i == 0:
                O[i][0] = 0
                O[i][1] = -prices[i]
            else:
                O[i][0] = max(O[i-1][0], O[i-1][1]+prices[i])
                O[i][1] = max(O[i-1][1], O[i-1][0]-prices[i])

        return O[-1][0]

