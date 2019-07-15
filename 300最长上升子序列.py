#  给定一个无序的整数数组，找到其中最长上升子序列的长度。
#  示例:
#  输入: [10,9,2,5,3,7,101,18]
#  输出: 4
#  解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#  说明:
    #  可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
    #  你算法的时间复杂度应该为 O(n2) 。
#  进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

#  动态规划
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        maxlenlist = [nums[0]]
        for i in range(len(nums)):
            #  如果当前值比最大上升子序列最后一个值大，加进上升子序列
            if nums[i] > maxlenlist[-1]:
                maxlenlist.append(nums[i])
            #  如果比最大上升子序列最后一个值小，
            #  将子序列中比当前值大的第一个数替换为当前值，
            #  这样不影响子序列的长度,
            #  如果后面出现更小的上升子序列可逐步替换之前的子序列
            elif nums[i] < maxlenlist[-1]:
                if len(maxlenlist) == 1:
                    maxlenlist[0] = nums[i]
                else:
                    #  把这个循环替换为二分查找，则时间复杂度为O(n log n)
                    for j in range(len(maxlenlist)-1):
                        if maxlenlist[j] < nums[i] and maxlenlist[j+1] > nums[i]:
                            maxlenlist[j+1] = nums[i]
                            break
        return len(maxlenlist)
