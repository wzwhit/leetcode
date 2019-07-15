#  给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#  示例 1:
#  输入: coins = [1, 2, 5], amount = 11
#  输出: 3
#  解释: 11 = 5 + 5 + 1
#  示例 2:
#  输入: coins = [2], amount = 3
#  输出: -1
#  说明:
#  你可以认为每种硬币的数量是无限的。

#  动态规划，f(n) = min(f(n - c1), f(n - c2), ... f(n - cn)) + 1
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 1:
            return 0
        if len(coins) < 1:
            return -1
        out = [-1 for i in range(amount+1)]
        out[0] = 0
        for i in range(1,amount+1):
            for j in coins:
                if j > i:
                    break
                if j == i:
                    out[i] = 1
                    break
                if j < i:
                    if out[i-j] == -1:
                        continue
                    elif out[i] == -1:
                        out[i] = out[i-j] + 1
                    else:
                        out[i] = min(out[i],out[i-j]+1)
        return out[-1]
