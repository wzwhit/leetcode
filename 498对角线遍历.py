#  给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
#  示例:
#  输入:
#  [
 #  [ 1, 2, 3 ],
 #  [ 4, 5, 6 ],
 #  [ 7, 8, 9 ]
#  ]
#  输出:  [1,2,4,7,5,3,6,8,9]
#  说明:
    #  给定矩阵中的元素总数不会超过 100000 。

#  超时
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return []
        m = len(matrix)
        n = len(matrix[0])
        p = 0
        out = []
        f = 0
        while p <= m + n - 2:
            if f == 0:
                l = min(n,p+1)
                for i in range(l):
                    if -1 < p-i < m and -1 < i < n:
                        out.append(matrix[p-i][i])
            else:
                l = min(m,p+1)
                for i in range(l):
                    if -1 < i < m and -1 < p-i < n:
                        out.append(matrix[i][p-i])
            f = 1 - f
            p += 1

        return out

#
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        M, N, result = len(matrix), len(matrix[0]), []
        for curve_line in range(M + N - 1):
            if curve_line < N:
                if curve_line % 2 == 0:
                    for i in range(min(M-1, curve_line), -1, -1):
                        # print(curve_line,i,result)
                        result.append(matrix[i][curve_line-i])
                else:
                    for i in range(min(M, curve_line + 1)):
                        # print(curve_line,i,result)
                        result.append(matrix[i][curve_line-i])
            else:
                if curve_line % 2 == 0:
                    for i in range(min(M-1, curve_line), curve_line - N, -1):
                        # print(curve_line,i,result)
                        result.append(matrix[i][curve_line-i])
                else:
                    for i in range(curve_line - N + 1, min(M, curve_line+1)):
                        # print(curve_line,i,result)
                        result.append(matrix[i][curve_line-i])
        return result

