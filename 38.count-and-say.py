#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (47.92%)
# Total Accepted:    20.3K
# Total Submissions: 42.4K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
# 
# 注意：整数顺序将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 
# 
#
class Solution:
    def countAndSay(self, n: 'int') -> 'str': 
        out = ['1']
        if n == 1:
            return out[0]                  
        for i in range(0,n-1):
            m = len(out[i])
            s = ''
            j = 0
            while True:
                if j < m-2 and out[i][j] == out[i][j+1] == out[i][j+2]:
                    s = s + str(3) + str(out[i][j])
                    j += 2
                    
                elif j < m-1 and out[i][j] == out[i][j+1]:
                    s = s + str(2) + str(out[i][j])
                    j += 1
                    
                elif (j < m-1 and out[i][j] != out[i][j+1]) or j == m-1:
                    s = s + str(1) + str(out[i][j])
                j += 1
                if j == m:
                    break
                    
            #print(s)
            out.append(s)
        return out[n-1]

        
