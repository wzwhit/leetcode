# -*- coding:utf-8 -*-
class Solution:
    def check(self, i, j, k):
        c = 0
        while i:
            c += i % 10
            i //= 10
        while j:
            c += j % 10
            j //= 10
        if c > k:
            return False
        else:
            return True

    def movingCount(self, threshold, rows, cols):
        # write code here
        count = [0]
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def helper(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if not visited[i][j] and self.check(i, j, threshold):
                count[0] += 1
                visited[i][j] = 1
                helper(i - 1, j)
                helper(i + 1, j)
                helper(i, j - 1)
                helper(i, j + 1)
            return

        helper(0, 0)
        return count[0]
s = Solution()
print(s.movingCount(5,10,10))