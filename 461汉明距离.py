#  两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#  给出两个整数 x 和 y，计算它们之间的汉明距离。
#  注意：
#  0 ≤ x, y < 231.
#  示例:
#  输入: x = 1, y = 4
#  输出: 2
#  解释:
#  1   (0 0 0 1)
#  4   (0 1 0 0)
       #  ↑   ↑
#  上面的箭头指出了对应二进制位不同的位置。

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        out = 0
        while x or y:
            a = x & 1
            b = y & 1
            out += a ^ b
            x >>= 1
            y >>= 1
        return out

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        out = 0
        a = x ^ y
        while a:
            a &= a-1
            out += 1
        return out
