#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.13%)
# Total Accepted:    79.2K
# Total Submissions: 281.6K
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ss = ''
        l = 0
        maxlen = 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(0,n):
            for j in range(i,n):
                if s[j] not in ss:
                    ss += s[j]
                    if j == n - 1:
                        l = j - i + 1
                else:
                    l = j - i
                    ss = ''
                    break
            if l > maxlen:
                        maxlen = l
        return maxlen

#  滑动窗口法
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        n = len(s)
        i = 0
        maxlen = 0
        for j in range(n):
            # print(i,j,maxlen)
            if s[j] not in s[i:j]:
                maxlen = max(maxlen, j-i+1)
            else:
                i += s[i:j].index(s[j]) + 1
        return maxlen

