# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
        self.minmum = float('inf')
    def push(self, node):
        # write code here
        self.stack.append(node)
        if node < self.minmum:
            self.minmum = node
        self.minstack.append(self.minmum)
    def pop(self):
        # write code here
        if self.stack:
            del self.minstack[-1]
            if self.minstack:
                self.minmum = self.minstack[-1]
            else:
                self.minmum = float('inf')
            return self.stack.pop()
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
    def min(self):
        # write code here
        return self.minmum