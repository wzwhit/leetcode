#  给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#  示例 1:
#  输入:
#  [
 #  [ 1, 2, 3 ],
 #  [ 4, 5, 6 ],
 #  [ 7, 8, 9 ]
#  ]
#  输出: [1,2,3,6,9,8,7,4,5]
#  示例 2:
#  输入:
#  [
  #  [1, 2, 3, 4],
  #  [5, 6, 7, 8],
  #  [9,10,11,12]
#  ]
#  输出: [1,2,3,4,8,12,11,10,9,5,6,7]

#  暴力
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        out = []
        for i in range(0, (m+1)//2):
            for j in range(i, n - i):
                out.append(matrix[i][j])
                count += 1
                if count == m*n:
                    return out
            for j in range(i+1, m-i-1):
                out.append(matrix[j][n-1-i])
                count += 1
                if count == m*n:
                    return out
            for j in range(n-1-i, -1+i, -1):
                out.append(matrix[m-1-i][j])
                count += 1
                if count == m*n:
                    return out
            for j in range(m-1-i-1, i, -1):
                out.append(matrix[j][i])
                count += 1
                if count == m*n:
                    return out
        return out

