#  给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#  示例:
#  输入: 3
#  输出:
#  [
 #  [ 1, 2, 3 ],
 #  [ 8, 9, 4 ],
 #  [ 7, 6, 5 ]
#  ]

#  54螺旋矩阵暴力螺旋遍历基础上改的
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        matrix = [[0 for j in range(n)] for i in range(n)]
        count = 0
        for i in range(0, (n+1)//2):
            for j in range(i, n - i):
                count += 1
                matrix[i][j] = count
                if count == n ** 2:
                    return matrix
            for j in range(i+1, n-i-1):
                count += 1
                matrix[j][n-1-i] = count
                if count == n ** 2:
                    return matrix
            for j in range(n-1-i, -1+i, -1):
                count += 1
                matrix[n-1-i][j] = count
                if count == n ** 2:
                    return matrix
            for j in range(n-1-i-1, i, -1):
                count += 1
                matrix[j][i] = count
                if count == n ** 2:
                    return matrix
        return matrix
