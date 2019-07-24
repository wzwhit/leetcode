#  编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
    #  每行的元素从左到右升序排列。
    #  每列的元素从上到下升序排列。

#  示例:
#  现有矩阵 matrix 如下：
#  [
  #  [1,   4,  7, 11, 15],
  #  [2,   5,  8, 12, 19],
  #  [3,   6,  9, 16, 22],
  #  [10, 13, 14, 17, 24],
  #  [18, 21, 23, 26, 30]
#  ]
#  给定 target = 5，返回 true。
#  给定 target = 20，返回 false。

#  按行遍历二分搜索，O(nlogn)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) < 1:
            return False
        if len(matrix[0]) < 1:
            return False
        def midsearch(nums, l, r):
            if not nums or l > r:
                return False
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
            return False
        out = False
        for i in range(len(matrix)):
            if matrix[i][-1] >= target >= matrix[i][0]:
                out = out or midsearch(matrix[i], 0, len(matrix[i])-1)
        return out

#  左下角开始，若相等return，若小于target则右移，若大于则上移
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) < 1:
            return False
        if len(matrix[0]) < 1:
            return False
        i, j = len(matrix)-1, 0
        while i > -1 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return False
