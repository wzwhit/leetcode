# -*- coding:utf-8 -*-
import sys

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            p = float(s)
            return True
        except:
            return False

while True:
    try:
        line = sys.stdin.readline().strip()
        if not line:
            break
        print(Solution().isNumeric(line))
    except:
        pass