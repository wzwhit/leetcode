#  给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#  示例 1:
#  输入:
#  11110
#  11010
#  11000
#  00000
#  输出: 1
#  示例 2:
#  输入:
#  11000
#  11000
#  00100
#  00011
#  输出: 3

#  广度优先搜索
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) < 1:
            return 0
        if len(grid[0]) < 1:
            return 0

        def helper(i, j, visited):
            if i < 0 or i > len(grid) -1 or j < 0 or j > len(grid[0]) -1:
                return visited
            if visited[i][j] == 1 and grid[i][j] == "1":
                visited[i][j] = 0
                visited = helper(i, j+1, visited)
                visited = helper(i, j-1, visited)
                visited = helper(i-1, j, visited)
                visited = helper(i+1, j, visited)
            return visited

        visited = [[1 for j in range(len(grid[0]))] for i in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 1 and grid[i][j] == "1":
                    count += 1
                    visited = helper(i,j, visited)
        return count
