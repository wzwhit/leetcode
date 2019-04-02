#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (42.12%)
# Total Accepted:    35.5K
# Total Submissions: 84.3K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        #print(n)
        bk = 0
        out = nums[0]
        i = 0       
        if n == 1:
            return nums[0]
        elif n > 1: 
            while i < n:
                lst = []
                sums = 0
                for j in range(i,n):
                    sums += nums[j]
                    lst.append(sums)
                lst.sort()
                bk = lst[-1]
                if bk > out:
                    out = bk
                i += 1
            return out

        
