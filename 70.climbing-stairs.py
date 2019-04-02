#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (43.79%)
# Total Accepted:    29.2K
# Total Submissions: 66.7K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 
#
class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        m = n // 2
        out = 1
        if m > 1:
            for i in range(1,m):  
                o = 1
                p = 1
                q = 1         
                for j in range(1,n-i+1):
                    o = o * j
                for r in range(1,i+1):
                    p = p * r
                for s in range(1,n-2*i+1):
                    q = q * s
                out += o // (p * q) #排列组合,计算C(n-i,i)=(n-i)! / ((n-i-i)! * i!)
        if n % 2 == 1 and n != 1:
            out += m + 1
        if n % 2 == 0 and n != 1:
            out += 1
        return out
