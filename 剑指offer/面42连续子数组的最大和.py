# -*- coding:utf-8 -*-
import sys
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        dp = [0 for _ in array]
        dp[0] = array[0]
        for i in range(1,len(array)):
            dp[i] = max(dp[i-1]+array[i],array[i])
        return max(dp)

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    line = [int(i) for i in line.split()]
    print(Solution().FindGreatestSumOfSubArray(line))