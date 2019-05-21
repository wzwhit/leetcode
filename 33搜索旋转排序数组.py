#  假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#  搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#  你可以假设数组中不存在重复的元素。
#  你的算法时间复杂度必须是 O(log n) 级别。
#  示例 1:
#  输入: nums = [4,5,6,7,0,1,2], target = 0
#  输出: 4
#  示例 2:
#  输入: nums = [4,5,6,7,0,1,2], target = 3
#  输出: -1

#  二分查找，递归
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        return self.midsearch(nums, 0, len(nums)-1, target)

    def midsearch(self, nums, left, right, target):
        if left >= right:
            return -1
        if target == nums[left] :
            return left
        if target == nums[right]:
            return right

        if nums[left] < target < nums[right]:
            mid = (left + right) // 2
        elif nums[left] > nums[right] and (target > nums[left] or target < nums[right]):
            mid = (left + right) // 2
        else:
            return -1

        k = self.midsearch(nums, left, mid, target)
        s = self.midsearch(nums, mid+1, right, target)
        return max(k,s)
