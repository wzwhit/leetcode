import sys
class Solution:
    def replaceSpace(self,s):
        if not s:
            return s
        ss = ''
        for i in s:
            if i == ' ':
                ss += '%20'
            else:
                ss += i
        return ss

if __name__ == "__main__":
    try:
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                break
            date = line
    except:
        pass

    print(Solution().replaceSpace(date))