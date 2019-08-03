#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (28.63%)
# Total Accepted:    17K
# Total Submissions: 59.3K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5
#
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss = s.split(' ')
        print(ss)
        if not ss:
            return 0
        i = len(ss) - 1
        while i >= 0:
            if ss[i] != '':
                return len(ss[i])
            else:
                i -= 1
        return 0
