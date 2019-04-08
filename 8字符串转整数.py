class Solution:
    def myAtoi(self, str: str) -> int:
        if str == '':
            return 0
        s = list(str)
        out = []
        i = j = 0
        output = 0
        while i < len(s):
            if s[i] == ' ' and i != len(s)-1:
                i += 1#找出第一个非空格字符
            elif s[i] == ' ' and i == len(s)-1:
                return 0#全是空格返回0
            else:
                if s[i] in ['+','-'] and i != len(s)-1:
                    out.append(s[i])
                    i += 1#i为第一个数字
                elif not s[i].isdigit():
                    return 0#第一个非空格字符不是+-或者数字，返回0
        j = i
        while j < len(s):
            if s[j].isdigit():
                j += 1#找到最长的连续数字
            else:
                if j == i:#如果连续数字长度为0，返回0
                    return 0
                break
        out.extend(s[i:j])#把连续数字串加到out里
        output = int(''.join(out))#list转字符串再转int
        if output > pow(2,31)-1:
            output = pow(2,31)-1
        if output < -pow(2,31):
            output = -pow(2,31)
        return output
