#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (24.46%)
# Total Accepted:    38K
# Total Submissions: 155.2K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = end = 0
        if n == 0 or n == 1:
            return s
        for i in range(0,n-1):
            l1 = self.maxlength(s,i,i)
            l2 = self.maxlength(s,i,i+1)
            maxlen = max(l1,l2)
            if maxlen > end - start + 1:
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2
        return s[start:end+1]


    def maxlength(self, s: str, i: int, j: int) -> int:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j - i - 1
        
        

