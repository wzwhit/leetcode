# -*- coding:utf-8 -*-
import sys
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        print(sequence)
        if len(sequence) < 1:
            return False
        left = 0
        for i in range(len(sequence) - 1):
            if sequence[i] > sequence[-1]:
                left = i
                break
            else:
                left += 1
        for j in range(left, len(sequence) - 1):
            if sequence[j] < sequence[-1]:
                return False
        l = True
        r = True
        if left > 0:
            l = self.VerifySquenceOfBST(sequence[:left])
        if left < len(sequence) - 1:
            r = self.VerifySquenceOfBST(sequence[left:len(sequence) - 1])
        return l and r

while True:
    line = sys.stdin.readline().strip()
    line = [int(i) for i in line.split()]
    print(Solution().VerifySquenceOfBST(line))
