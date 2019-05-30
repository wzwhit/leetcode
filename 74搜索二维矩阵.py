#  编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
    #  每行中的整数从左到右按升序排列。
    #  每行的第一个整数大于前一行的最后一个整数。
#  示例 1:
#  输入:
#  matrix = [
  #  [1,   3,  5,  7],
  #  [10, 11, 16, 20],
  #  [23, 30, 34, 50]
#  ]
#  target = 3
#  输出: true
#  示例 2:
#  输入:
#  matrix = [
  #  [1,   3,  5,  7],
  #  [10, 11, 16, 20],
  #  [23, 30, 34, 50]
#  ]
#  target = 13
#  输出: false

#  二分法
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        a = []
        for i in range(len(matrix)):
            a.extend(matrix[i])

        def midsearch(a, i, j):
            if i > j :
                return False
            mid = (i + j) // 2
            while i <= mid:
                if a[i] == target:
                    return True
                i += 1
            while j > mid:
                if a[j] == target:
                    return True
                j -= 1
            return midsearch(a, i, mid) or midsearch(a, mid+1, j)
        return midsearch(a, 0, len(a)-1)
