# -*- coding:utf-8 -*-
import sys


# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        if len(numbers) == 1:
            return numbers[0]

        def patition(num, i, j):
            k = i
            while i < j:
                while i < j and num[j] >= num[k]:
                    j -= 1
                while i < j and num[i] <= num[k]:
                    i += 1
                num[i], num[j] = num[j], num[i]
            num[i], num[k] = num[k], num[i]
            return i

        def quicksort(num, i, j):
            if i >= j:
                return i
            mid = patition(num, i, j)
            print(mid,i,j,num)
            if mid == len(numbers) // 2:
                print(mid)
                return mid
            if mid > len(numbers) // 2:
                return quicksort(num, i, mid - 1)
            else:
                return quicksort(num, mid + 1, j)

        index = quicksort(numbers, 0, len(numbers) - 1)
        n = 0
        for i in numbers:
            if i == numbers[index]:
                n += 1
        if n > len(numbers)//2:
            return numbers[index]
        else:
            return 0

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    line = [int(i) for i in line.split()]
    print(Solution().MoreThanHalfNum_Solution(line))