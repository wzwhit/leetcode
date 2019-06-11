#  假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#  ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#  编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#  示例 1:
#  输入: nums = [2,5,6,0,0,1,2], target = 0
#  输出: true
#  示例 2:
#  输入: nums = [2,5,6,0,0,1,2], target = 3
#  输出: false
#  进阶:

    #  这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
    #  这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

#  33搜索排序数组二分法基础上考虑两端相等的特殊情况
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def midsearch(l, r):
            #print(l,r)
            if l > r:
                return False
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[r]:
                return midsearch(l,mid-1) or midsearch(mid+1,r)
            else:
                if nums[l] <= target <= nums[mid]:
                    return midsearch(l, mid-1)
                else:
                    return midsearch(mid+1, r)
            return False

        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            #print(l,r,mid)
            if nums[l] < nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    return midsearch(l,mid)
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if nums[mid] <= target <= nums[r]:
                    return midsearch(mid,r)
                else:
                    r = mid - 1
            elif nums[l] == nums[mid]:
                return midsearch(l,mid) or midsearch(mid+1,r)
        return False
