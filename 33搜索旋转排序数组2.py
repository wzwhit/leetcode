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

#  从中间分开，左右有个一为有序，在有序里进行二分查找，找不到在另一边无序里再次从中间分开，循环直到找到为止
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    return self.midsearch(nums, left, mid,target)
                else:
                    left = mid+1
            else:
                if nums[mid] <= target <= nums[right]:
                    return self.midsearch(nums, mid, right, target)
                else:
                    right = mid-1
        return -1
        
    def midsearch(self, nums, left, right, target): 
        print(left, right)
        if left > right:
            return -1
        mid = (left+right) // 2       
        if nums[mid] == target:
            return mid
        if nums[left] <= target <= nums[mid]:       
            return self.midsearch(nums, left, mid-1,target)
        else:
            return self.midsearch(nums, mid+1, right,target)
        return -1
