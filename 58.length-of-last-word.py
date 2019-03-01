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
#
class Solution:
    def lengthOfLastWord(self, s: 'str') -> 'int':
        input = list(s)
        n = len(input)
        m = 0
        if n == 0 or (n == 1 and input[0] == ' '):
            return 0
        elif n == 1 and input[0] != ' ':
            return 1
        elif n > 1:           
            for i in range(n-1,-1,-1):
                if input[i] != ' ':
                    m = 1
                    break
            if m == 0:
                return 0
            elif m == 1:
                for j in range(i,-1,-1):
                    if j == 0 and input[j] != ' ':
                        return i+1
                    elif input[j] == ' ':
                        return i-j

        
