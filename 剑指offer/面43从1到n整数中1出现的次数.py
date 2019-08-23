# -*- coding:utf-8 -*-
import sys
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 10:
            return 1
        count = 0
        nn = n
        length = 0
        while nn:
            length += 1
            nn //= 10
        while n:
            print(n,count,length)
            if n // (10**(length-1)) == 1:
                count += n % (10**(length-1))+1
            elif n // (10**(length-1)) > 1:
                count += 10**(length-1)
            elif n // (10**(length-1)) == 0:
                if n % (10 ** (length - 1)) >= 1:
                    count += 1
            # if n % 10**(length-1) == 0:
            n = 10**(length-1) - 1
            # else: n %= 10**(length-1)
            length -= 1
        return count

while True:
    n = sys.stdin.readline().strip()
    if not n:
        break
    n = int(n)
    print(Solution().NumberOf1Between1AndN_Solution(n))