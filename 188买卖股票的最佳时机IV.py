#  给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#  注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#  示例 1:
#  输入: [2,4,1], k = 2
#  输出: 2
#  解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
#  示例 2:
#  输入: [3,2,6,5,0,3], k = 2
#  输出: 7
#  解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     #  随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。


#  动态规划，与题122、121、123一样，这里k可能特别大，所以会超时
#  一笔交易至少要两天，所以k <= N/2
#  如果k > N/2，就相当于没有限制次数,与题122一样，直接调用题122
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def maxProfit(prices):
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

        N = len(prices)
        if N < 2 or k < 1:
            return 0
        if k > N/2:
            return maxProfit(prices)

        O = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(N)]
        for n in range(N):
            for kk in range(1,k+1):#所有值初始化为0，所以k从1开始
                if n == 0 and kk != 0:
                    O[n][kk][0] = 0
                    O[n][kk][1] =  -prices[n]
                else:
                    O[n][kk][0] = max(O[n-1][kk][0], O[n-1][kk][1]+prices[n])
                    O[n][kk][1] = max(O[n-1][kk][1], O[n-1][kk-1][0]-prices[n])
        return O[-1][-1][0]
