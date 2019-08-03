#  给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#  返回被除数 dividend 除以除数 divisor 得到的商。
#  示例 1:
#  输入: dividend = 10, divisor = 3
#  输出: 3
#  示例 2:
#  输入: dividend = 7, divisor = -3
#  输出: -2

#  说明:
    #  被除数和除数均为 32 位有符号整数。
    #  除数不为 0。
    #  假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

#  要求商，我们首先想到的是减法，能被减多少次，那么商就为多少，但是明显减法的效率太低
#  那么我们可以用位移法，因为计算机在做位移时效率特别高，向左移1相当于乘以2，向右位移1相当于除以2
#  我们可以把一个dividend（被除数）先除以2^n，n最初为31，不断减小n去试探,当某个n满足dividend/2^n >= divisor时，
#  表示我们找到了一个足够大的数，这个数*divisor是不大于dividend的，所以我们就可以减去2^n个divisor，以此类推
#  我们可以以100/3为例
#  2^n是1，2，4，8...2^31这种数，当n为31时，这个数特别大，100/2^n是一个很小的数，肯定是小于3的，所以循环下来，
#  当n=5时，100/32=3, 刚好是大于等于3的，这时我们将100-32*3=4，也就是减去了32个3，接下来我们再处理4，同样手法可以再减去一个3
#  所以一共是减去了33个3，所以商就是33

#  每次都从2^0+2^1+...开始逼近，当快要接近被除数时。再从2^0+2^1+...开始逼近。直到不能更近为止。
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        out = 0
        dividend1 = abs(dividend)
        divisor1 = abs(divisor)
        n = 31

        while dividend1 >= divisor1:
            last = dividend1
            dividend1 >>= n

            if dividend1 >= divisor1:
                out += 1<<n
                dividend1 = last - (divisor1 << n)
                continue
            n -= 1
            dividend1 = last

        if dividend ^ divisor < 0:
            out = -out
        if out < -2**31 or out > 2**31-1:
            out = 2**31-1
        return out
