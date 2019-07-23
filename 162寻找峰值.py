#  峰值元素是指其值大于左右相邻值的元素。
#  给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#  数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#  你可以假设 nums[-1] = nums[n] = -∞。
#  示例 1:
#  输入: nums = [1,2,3,1]
#  输出: 2
#  解释: 3 是峰值元素，你的函数应该返回其索引 2。
#  示例 2:
#  输入: nums = [1,2,1,3,5,6,4]
#  输出: 1 或 5
#  解释: 你的函数可以返回索引 1，其峰值元素为 2；
     #  或者返回索引 5， 其峰值元素为 6。
#  说明:
#  你的解法应该是 O(logN) 时间复杂度的。


#  O(logN)优先想到二分查找
#  首先从数组 numsnumsnums 中找到中间的元素mid。
#  若该元素恰好位于降序序列或者一个局部下降坡度中（通过将 nums[i] 与右侧比较判断)
#  则说明峰值会在本元素的左边。于是，我们将搜索空间缩小为 mid 的左边(包括其本身)，
#  并在左侧子数组上重复上述过程。

#  若该元素恰好位于升序序列或者一个局部上升坡度中（通过将 nums[i] 与右侧比较判断)，
#  则说明峰值会在本元素的右边。于是，我们将搜索空间缩小为 mid 的右边，
#  在右侧子数组上重复上述过程。
#  就这样，我们不断地缩小搜索空间，直到搜索空间中只有一个元素，该元素即为峰值元素。
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        def midsearch(nums, l, r):
            if l > r:
                return -1
            while l <= r:
                mid = l + (r - l) // 2
                if 0 < mid < len(nums)-1:
                    if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                        return mid
                elif mid == 0:
                    if nums[mid] > nums[mid+1]:
                        return mid
                elif mid == len(nums)-1:
                    if nums[mid] > nums[mid-1]:
                        return mid
                if mid < len(nums) and nums[mid] > nums[mid+1]:
                    r = mid - 1
                if mid < len(nums) and nums[mid] < nums[mid+1]:
                    l = mid + 1
            return -1

        return midsearch(nums, 0, len(nums)-1)

