# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix:
            return False
        if not matrix[0]:
            return False

        def helper(i, j, p, v):
            if not p:
                return True
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1 or v[i][j]:
                return False
            if matrix[i * cols + j] == p[0]:
                v[i][j] = 1
                return helper(i - 1, j, p[1:], v) or helper(i + 1, j, p[1:], v) or helper(i, j - 1, p[1:], v) or helper(
                    i, j + 1, p[1:], v)
            else:
                return False

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i * cols + j] == path[0]:
                    v = [k[:] for k in visited]
                    if helper(i, j, path, v):
                        return True
        return False

s = Solution()
print(s.hasPath("AAAAAAAAAAAA",3,4,"AAAAAAAAAAAA"))