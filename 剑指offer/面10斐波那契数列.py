# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        # 递归太慢，不如直接循环或者说动态规划
        if n <= 1:
            return n
        n1 = 0
        n2 = 1
        out = 0
        for i in range(2,n+1):
            out = n1 + n2
            n1, n2 = n2, out
        return out