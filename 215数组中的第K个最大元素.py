#  在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#  示例 1:
#  输入: [3,2,1,5,6,4] 和 k = 2
#  输出: 5
#  示例 2:
#  输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
#  输出: 4
#  说明:
#  你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

# 双路快排超时
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(nums):
            def partition(nums, l, r):
                k = l
                while l < r:
                    while l < r and nums[r] >= nums[k]:
                        r -= 1
                    while l < r and nums[l] <= nums[k]:
                        l += 1
                    nums[l], nums[r] = nums[r], nums[l]
                nums[l], nums[k] = nums[k], nums[l]
                return l
            def qsort(nums, l, r):
                if l >= r:
                    return
                mid = partition(nums, l, r)
                qsort(nums, l, mid-1)
                qsort(nums, mid+1, r)

            if len(nums) <= 1:
                return
            qsort(nums, 0, len(nums)-1)
            return

        quicksort(nums)
        #  nums.sort()
        return nums[-k]

#  双路快排改进为快速选择，根据key划分数组，找到n-k个元素在左边还是右边,
#  只排序n-k所在的一边就行
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(nums):
            def partition(nums, l, r):
                k = l
                while l < r:
                    while l < r and nums[r] >= nums[k]:
                        r -= 1
                    while l < r and nums[l] <= nums[k]:
                        l += 1
                    nums[l], nums[r] = nums[r], nums[l]
                nums[l], nums[k] = nums[k], nums[l]
                return l
            def qsort(nums, l, r):
                if l >= r:
                    return
                mid = partition(nums, l, r)
                if mid > len(nums) - k:# 划分数组找到n-k所在的区域,对其进行排序
                    qsort(nums, l, mid-1)
                elif mid < len(nums) - k:
                    qsort(nums, mid+1, r)
                else:
                    return

            if len(nums) <= 1:
                return
            qsort(nums, 0, len(nums)-1)
            return

        quicksort(nums)
        # nums.sort()
        return nums[-k]
