#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.59%)
# Total Accepted:    48.7K
# Total Submissions: 154K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        input = list(strs)
        n = len(input)
        if n == 0:
            return ""
        if n == 1:
            return input[0]
        q = len(input[0])
        if q == 0:
            return ""
        for i in range(0,n):
            p = len(input[i])           
            if p < q:
                q = p
        for i in range(0,q):
            for j in range(0,n-1):
                if input[j][i] != input[j+1][i]:
                    if i == 0:
                        return ""
                    else:
                        return input[0][0:i]
        return input[0][0:q]

        
        
