#  给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#  说明：本题中，我们将空字符串定义为有效的回文串。
#  示例 1:
#  输入: "A man, a plan, a canal: Panama"
#  输出: true
#  示例 2:
#  输入: "race a car"
#  输出: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # 大写转小写
        a = []
        for i in range(len(s)):
            # 判断是不是字母或者数字
            if '0' <= s[i] <= '9' or 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
                a.append(s[i])
        return a == a[::-1]
