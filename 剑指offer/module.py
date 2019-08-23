import sys

class Solution:
    def minimumTotal(self, triangle):
        # input List[List[]]
        # retun int
        if not triangle:
            return 0
        if not triangle[0]:
            return 0
        dp = [[triangle[i][j] for j in range(len(triangle[i]))] for i in range(len(triangle))]
        print(dp)
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] += dp[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] += dp[i - 1][j - 1]
                else:
                    dp[i][j] += min(dp[i-1][j], dp[i-1][j-1])

        return min(dp[-1][:])


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    date = []
    i = 0
    try:
        while True:
            i += 1
            line = sys.stdin.readline().strip()
            # line = input()
            if line == '':
                break
            lines = line.split()#字符串
            values = list(map(int, lines))#转成整数
            date.append(values)
            if i == n:
                solu = Solution()
                out = solu.minimumTotal(date)
                print(out)
                date = []
                i = 0
    except:
        pass


