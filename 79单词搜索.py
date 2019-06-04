#  给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#  示例:
#  board =
#  [
  #  ['A','B','C','E'],
  #  ['S','F','C','S'],
  #  ['A','D','E','E']
#  ]
#  给定 word = "ABCCED", 返回 true.
#  给定 word = "SEE", 返回 true.
#  给定 word = "ABCB", 返回 false.

#  回溯法
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def around(i,j,w,visited):
            if i < 0 or j < 0 or i > m-1 or j > n-1:
                return
            #print(i,j,w)
            if w == []:
                o.append(1)
                return
            if board[i][j] == w[0] and [i,j] not in visited and len(o) == 0:
                visited.append([i,j])
                around(i,j-1,w[1:],visited)
                around(i,j+1,w[1:],visited)
                around(i-1,j,w[1:],visited)
                around(i+1,j,w[1:],visited)
                visited.pop()

        m = len(board)
        n = len(board[0])
        o = []
        w = list(word)
        k = len(w)
        if m < 1 or n < 1 or k < 1:
            return False
        if k == 1:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == w[0]:
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == w[0]:
                    around(i,j,w,[])

        return len(o) > 0
