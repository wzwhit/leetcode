#  给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#  例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#  与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

#  与15题三数之和类似，先排序，遍历数值指定第一个数，双指针找其他两个数,O(n*2)时间复杂度
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 0
        nums.sort()
        closesum = 0
        minerror = 100000000
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                error = sum - target
                if error == 0:
                    return sum
                if abs(error) < minerror:
                    minerror = abs(error)
                    closesum = sum
                if error > 0:
                    r -= 1
                else:
                    l += 1
        return closesum
