#  实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#  必须原地修改，只允许使用额外常数空间。
#  以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
#  1,2,3 → 1,3,2
#  3,2,1 → 1,2,3
#  1,1,5 → 1,5,1

#  1.从后向前找相邻两数nums[i]>nums[i-1]
#  2.从i往后找比nums[i-1]大的最小的数nums[j]，因为i之后的数已经是降序排列，
#    只要从后往前找到第一个比nums[i-1]大的数即可
#  3.交换nums[i-1]和nums[j]
#  4.排序i之后的数即为所要的数，因为后面的数都是降序排列，所以直接倒序即可
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                for j in range(n-1,i-1,-1):
                    if nums[j] > nums[i-1]:
                        a = nums[i-1]
                        nums[i-1] = nums[j]
                        nums[j] = a
                        break
                for k in range(i, (n+i)//2):
                    (nums[k],nums[n-1-k+i]) = (nums[n-1-k+i],nums[k])
                return
        nums.sort()
