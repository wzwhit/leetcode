# -*- coding:utf-8 -*-
import sys

class Solution:
    def NumberOf1(self, n):
        # write code here
        if not n:
            return 0
        count = 0
        # python负数前面有无穷个1,所以n & 0xffffffff后变成32位的正数,但每一位的数值并没有变
        n = n & 0xffffffff
        while n:
            # (n - 1) & n 后右边第一个1变成0,前面都不变
            n = (n-1) & n
            count += 1
        return count

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print(n)
    print(Solution().NumberOf1(n))
