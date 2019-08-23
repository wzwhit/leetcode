import sys

class Solution:
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False
        i = 0
        while i < len(numbers):
            if numbers[i] == i:
                i += 1
                continue
            elif numbers[i] != i and numbers[numbers[i]] != numbers[i]:
                j = numbers[i]
                numbers[i], numbers[j] = numbers[j], numbers[i]
            elif numbers[i] != i and numbers[numbers[i]] == numbers[i]:
                duplication[0] = numbers[i]
                print(numbers[i])
                return True
        return False


if __name__ == "__main__":
    try:

        while True:
            line = sys.stdin.readline().strip()
            if not line:
                break
            line = line.split()
            # date = list(map(int,line))
            date = [int(i) for i in line]
    except:
        pass
    flag = Solution().duplicate(date,date)
