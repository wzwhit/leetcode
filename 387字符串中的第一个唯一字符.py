#  给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#  案例:
#  s = "leetcode"
#  返回 0.
#  s = "loveleetcode",
#  返回 2.

#  hash table,两次遍历
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        for i in s:
            if hash.get(i) != None:
                hash[i] += 1
            else:
                hash[i] = 1
        for i in range(len(s)):
            if hash.get(s[i]) == 1:
                return i
        return -1
