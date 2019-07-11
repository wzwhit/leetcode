#  给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#  示例 1:
#  输入:
#  [
  #  [1,1,1],
  #  [1,0,1],
  #  [1,1,1]
#  ]
#  输出:
#  [
  #  [1,0,1],
  #  [0,0,0],
  #  [1,0,1]
#  ]
#  示例 2:
#  输入:
#  [
  #  [0,1,2,0],
  #  [3,4,5,2],
  #  [1,3,1,5]
#  ]
#  输出:
#  [
  #  [0,0,0,0],
  #  [0,4,5,0],
  #  [0,3,1,0]
#  ]
#  进阶:
    #  一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
    #  一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
    #  你能想出一个常数空间的解决方案吗？

#  空间O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix == [] or matrix == [[]]:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        i = j = 0
        a = []
        b = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    a.append(i)
                    b.append(j)
        for i in a:
            for j in range(n):
                matrix[i][j] = 0
        for i in b:
            for j in range(m):
                matrix[j][i] = 0

#  常数空间是用矩阵行列第一个数作为标记是否置零，用一个常数记录区分首行和首列
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m < 1:
            return matrix
        n = len(matrix[0])
        if n < 1:
            return matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if (i != 0 and j != 0) or (i == 0 and j == 0):
                        matrix[i][0] = 'wzw'
                        matrix[0][j] = 'wzw'
                    elif i == 0:
                        if matrix[0][0] != 'wzw' and matrix[0][0] != 'col':
                            matrix[0][0] = 'row'
                        elif matrix[0][0] == 'col':
                            matrix[0][0] = 'wzw'
                        matrix[0][j] = 'wzw'
                    elif j == 0:
                        if matrix[0][0] != 'wzw' and matrix[0][0] != 'row':
                            matrix[0][0] = 'col'
                        elif matrix[0][0] == 'row':
                            matrix[0][0] = 'wzw'
                        matrix[i][0] = 'wzw'
        print(matrix)
        for i in range(1,m):
            if matrix[i][0] == 'wzw':
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(1,n):
            if matrix[0][j] == 'wzw':
                for i in range(m):
                    matrix[i][j] = 0
        if matrix[0][0] == 'wzw':
            for i in range(m):
                matrix[i][0] = 0
            for j in range(n):
                matrix[0][j] = 0
        elif matrix[0][0] == 'row':
            for j in range(n):
                matrix[0][j] = 0
        elif matrix[0][0] == 'col':
            for i in range(m):
                matrix[i][0] = 0
