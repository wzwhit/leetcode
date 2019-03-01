#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (46.33%)
# Total Accepted:    16.2K
# Total Submissions: 34.9K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 
# 输入为非空字符串且只包含数字 1 和 0。
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1 = list(a)
        b1 = list(b)
        la = len(a1)
        lb = len(b1)
        sum = []
        add = []       
        if la > lb:
            for n in a1:
                sum.append(int(n))
            for n in b1:
                add.append(int(n))
        else:
            for n in b1:
                sum.append(int(n))
            for n in a1:
                add.append(int(n))
        for i in range(0,abs(la-lb)):
            add[0:0] = [0]
        jin = 0
        for i in range(len(sum)-1,-1,-1):
            if sum[i] + add[i] + jin == 0:
                sum[i] = 0
                jin = 0
            elif sum[i] + add[i] + jin == 1:
                sum[i] = 1
                jin = 0
            elif sum[i] + add[i] + jin == 2:
                sum[i] = 0
                jin = 1
            elif sum[i] + add[i] + jin == 3:
                sum[i] = 1
                jin = 1       
        if jin == 1:
            sum[0:0] = [1]  

        lst=[str(i) for i in sum]  
        out=''.join(lst)                                                                                                       
        return out
            

