# -*- coding:utf-8 -*-
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k > len(tinput):
            return []
        heap = []
        for i in tinput:
            heapq.heappush(heap,i)
        out = []
        for _ in range(k):
            out.append(heapq.heappop(heap))
        return out