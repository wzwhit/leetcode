# -*- coding:utf-8 -*-
import sys
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return []
        if not matrix[0]:
            return []
        out = []
        while matrix:
            for i in matrix[0]:
                out.append(i)
            matrix = list(zip(*matrix[1:]))
            matrix = matrix[::-1]
        return out

n = int(sys.stdin.readline().strip())
data = []
i = 0
while True:
    i += 1
    line = sys.stdin.readline().strip()
    if not line:
        break
    line = [int(i) for i in line.split()]
    data.append(line)
    if i == n:
        print(Solution().printMatrix(data))
        data = []
        i = 0
