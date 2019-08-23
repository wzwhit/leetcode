# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        out = []
        def backtrack(s,tmp):
            if len(tmp) == len(ss):
                if tmp not in out:
                    out.append(tmp)
                return
            if not s:
                return
            for i in range(len(s)):
                backtrack(s[:i]+s[i+1:], tmp+[s[i]])
        backtrack(ss,[])
        out = [''.join(i) for i in out]
        return out