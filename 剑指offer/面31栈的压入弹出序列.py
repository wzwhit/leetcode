# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        stack = []
        for i in pushV:
            if i == popV[0]:
                popV = popV[1:]
                continue
            else:
                stack.append(i)
        for i in range(len(stack)-1, -1, -1):
            if stack[i] != popV[len(stack)-1-i]:
                return False
        return True