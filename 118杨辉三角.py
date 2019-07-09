#  给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#  示例:
#  输入: 5
#  输出:
#  [
     #  [1],
    #  [1,1],
   #  [1,2,1],
  #  [1,3,3,1],
 #  [1,4,6,4,1]
#  ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        out = [[1],[1,1]]
        for i in range(2,numRows):
            row = [1]
            for j in range(len(out[i-1])-1):
                row.append(out[i-1][j] + out[i-1][j+1])
            row.append(1)
            out.append(row)
        return out
