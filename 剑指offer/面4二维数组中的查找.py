import sys
class Solution:
    def Find(self, target, array):
        if not array:
            return False
        if not array[0]:
            return False
        i = len(array) - 1
        j = 0
        while i > -1 and j < len(array[0]):
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                j += 1
            elif array[i][j] > target:
                i -= 1
        return False

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    try:
        date = []
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                break
            line = line.split()
            line = list(map(int,line))
            date.append(line)
    except:
        pass

    print(Solution().Find(n,date))
