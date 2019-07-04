#  统计所有小于非负整数 n 的质数的数量。
#  示例:
#  输入: 10
#  输出: 4
#  解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

#  厄拉多塞筛法，每找到一个质数就把他的倍数给删掉
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        nums = [1 if i>1 else 0 for i in range(0,n)]

        for i in range(2,int(n**0.5)+1):
            if nums[i] == 1:
                nums[i*i::i] = [0] * len(nums[i*i::i])

        return sum(nums)
