#  给定一个没有重复数字的序列，返回其所有可能的全排列。
#  示例:
#  输入: [1,2,3]
#  输出:
#  [
  #  [1,2,3],
  #  [1,3,2],
  #  [2,1,3],
  #  [2,3,1],
  #  [3,1,2],
  #  [3,2,1]
#  ]

#  回溯
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        out = []
        def backtrack(nums, tmp):
            print(nums,tmp)
            if not nums:
                out.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], tmp+[nums[i]])
        backtrack(nums,[])
        return out
