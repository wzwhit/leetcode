#  给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
#  数学表达式如下:
    #  如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
    #  使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
#  说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
#  示例 1:
#  输入: [1,2,3,4,5]
#  输出: true
#  示例 2:
#  输入: [5,4,3,2,1]
#  输出: false

#  记录最小值和次小值，找后面比次小值大的数
#  若后面数比最小值小，更新最小值，若比最小值大次小值小，更新次小值
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        minmum = float('inf')
        secondmin = float('inf')
        for i in range(len(nums)):
            # print(minmum,secondmin,i)
            if nums[i] < minmum:
                minmum = nums[i]
            elif nums[i] > minmum and nums[i] < secondmin:
                secondmin = nums[i]
            elif nums[i] > secondmin:
                return True
        return False
