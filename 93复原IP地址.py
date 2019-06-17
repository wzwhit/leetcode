#  给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#  示例:
#  输入: "25525511135"
#  输出: ["255.255.11.135", "255.255.111.35"]

#  回溯法
#  IP的格式,共四位,每位是在0~255之间,
#  注意: 不能出现以0开头的两位以上数字,比如012,08
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        out = []
        def backtrack(i, tmp):
            if i > 0 and (int(tmp[-1]) > 255 or len(tmp) > 4 or (tmp[-1][0] == '0' and len(tmp[-1]) > 1)):
                return
            if i == len(s) and len(tmp) == 4:
                tmp = [str(i) for i in tmp]
                tmp = '.'.join(tmp)
                out.append(tmp)
                return
            if i == len(s):
                return
            if i > 0:
                backtrack(i+1,tmp[:-1]+[tmp[-1]+s[i]])
            backtrack(i+1,tmp+[s[i]])
            return
        backtrack(0,[])
        return out
