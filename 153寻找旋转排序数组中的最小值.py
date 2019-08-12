#  假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#  请找出其中最小的元素。
#  你可以假设数组中不存在重复元素。
#  示例 1:
#  输入: [3,4,5,1,2]
#  输出: 1
#  示例 2:
#  输入: [4,5,6,7,0,1,2]
#  输出: 0

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -float('inf')

        return self.midSearch(nums, 0, len(nums)-1)

    def midSearch(self,nums,i,j):
        if i > j:
            return -float('inf')
        if i == j:
            return nums[i]
        while i < j:
            print(i,j)
            mid = (i + j) // 2
            if nums[mid] > nums[i] and nums[mid] > nums[j]:
                i = mid + 1
            elif nums[mid] < nums[i] and nums[mid] < nums[j]:
                j = mid
            elif nums[mid] >= nums[i] and nums[mid] < nums[j]:
                return nums[i]
            elif nums[mid] <= nums[i] and nums[mid] > nums[j]:
                return nums[j]
        return nums[i]

