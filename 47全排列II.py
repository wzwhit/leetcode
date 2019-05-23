#  给定一个可包含重复数字的序列，返回所有不重复的全排列。
#  示例:
#  输入: [1,1,2]
#  输出:
#  [
  #  [1,1,2],
  #  [1,2,1],
  #  [2,1,1]
#  ]

#  回溯法，46题基础上去重
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
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
                if i > 0 and nums[i] == nums[i-1]:#去重
                    continue
                backtrack(nums[:i]+nums[i+1:], tmp+[nums[i]])
        backtrack(nums,[])
        return out
