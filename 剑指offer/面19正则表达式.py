# -*- coding:utf-8 -*-
import sys
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not s and not pattern:
            return True
        elif not pattern:
            return False
        elif not s:
            for i in range(len(pattern)):
                if pattern[i] != '*':
                    if i< len(pattern)-1 and pattern[i+1] == '*':
                        continue
                    else:
                        return False
            return True
        def helper(i,j):
            if i > len(s)-1 and j > len(pattern)-1:
                return True
            if i < len(s) and j > len(pattern)-1:
                return False
            if j < len(pattern)-1 and pattern[j+1] == '*':
                if (i < len(s) and pattern[j] == s[i]) or (i < len(s) and pattern[j] == '.'):
                    return helper(i,j+2) or helper(i+1,j+2) or helper(i+1,j)
                else: return helper(i,j+2)
            if i < len(s) and j < len(pattern) and s[i] == pattern[j] or (i < len(s) and pattern[j] == '.'):
                return helper(i+1,j+1)
            return False

        return helper(0,0)

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    pattern = sys.stdin.readline().strip()
    print(s,pattern)
    print(Solution().match(s,pattern))