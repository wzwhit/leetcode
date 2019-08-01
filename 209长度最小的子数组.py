#  给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#  示例:
#  输入: s = 7, nums = [2,3,1,2,4,3]
#  输出: 2
#  解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
#  进阶:
#  如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        i, j, nsum = 0, 0, 0
        minl = len(nums) + 1
        while i < len(nums) and i <= j:
            if nsum >= s:
                if j-i < minl:
                    minl = j-i
                nsum -= nums[i]
                i += 1
            elif nsum < s:
                if j < len(nums):
                    nsum += nums[j]
                    j += 1
                else:
                    break
        if minl > len(nums):
            return 0
        else:
            return minl
