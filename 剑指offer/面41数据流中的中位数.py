# -*- coding:utf-8 -*-
import heapq
import sys

class Solution:
    def __init__(self):
        self.leftmax = []
        self.rightmin = []
        self.i = 0

    def Insert(self, num):
        # write code here
        self.i += 1
        if self.i % 2 == 1:
            heapq.heappush(self.rightmin, num)
            heapq.heappush(self.leftmax, -heapq.heappop(self.rightmin))
        else:
            heapq.heappush(self.leftmax, -num)
            heapq.heappush(self.rightmin, -heapq.heappop(self.leftmax))

    def GetMedian(self,data):
        # write code here
        print(self.leftmax,self.rightmin)
        if self.i % 2 == 1:
            return -heapq.nsmallest(1,self.leftmax)[0]
        else:
            if self.leftmax and self.rightmin:
                return (-heapq.nsmallest(1,self.leftmax)[0] + heapq.nsmallest(1,self.rightmin)[0]) / 2.0

s = Solution()
while True:
    n = sys.stdin.readline().strip()
    if not n:
        break
    n = int(n)
    s.Insert(n)
    print(s.GetMedian())

# # -*- coding:utf-8 -*-
# class Solution:
#     def __init__(self):
#         self.nums = []
#     def Insert(self, num):
#         # write code here
#         self.nums.append(num)
#         self.nums.sort()
#     def GetMedian(self,data):
#         # write code here
#         if len(self.nums) > 0:
#             if len(self.nums) % 2 == 1:
#                 return self.nums[len(self.nums)/2]
#             else:
#                 return (self.nums[len(self.nums)/2] + self.nums[len(self.nums)/2-1])/2.0

