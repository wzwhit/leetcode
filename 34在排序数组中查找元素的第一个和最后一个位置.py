#  给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#  你的算法时间复杂度必须是 O(log n) 级别。
#  如果数组中不存在目标值，返回 [-1, -1]。
#  示例 1:
#  输入: nums = [5,7,7,8,8,10], target = 8
#  输出: [3,4]
#  示例 2:
#  输入: nums = [5,7,7,8,8,10], target = 6
#  输出: [-1,-1]

#  二分法找到一个目标位置，从目标位置往左右两侧延伸
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1,-1]
        left, right = 0, n-1
        out = [-1,-1]
        p = self.midsearch(nums, left, right, target)
        if p == -1:
            return [-1,-1]
        else:
            s1 = s2 = p
            while s1 > 0 and nums[s1] == nums[s1-1]:
                s1 -= 1
            while s2 < n-1 and nums[s2] == nums[s2+1]:
                s2 += 1
            out = [s1,s2]
            return sorted(out)

    def midsearch(self, nums, left, right,target):
        if left > right:
            return -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1
