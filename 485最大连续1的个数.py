#  给定一个二进制数组， 计算其中最大连续1的个数。
#  示例 1:
#  输入: [1,1,0,1,1,1]
#  输出: 3
#  解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#  注意：
    #  输入的数组只包含 0 和1。
    #  输入数组的长度是正整数，且不超过 10,000。


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxlen = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                l = 1
                while i < len(nums)-1 and nums[i] == nums[i+1] == 1:
                    i += 1
                    l += 1
                if l > maxlen:
                    maxlen = l
            i += 1
        return maxlen

