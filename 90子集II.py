#  给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#  说明：解集不能包含重复的子集。
#  示例:
#  输入: [1,2,2]
#  输出:
#  [
  #  [2],
  #  [1],
  #  [1,2,2],
  #  [2,2],
  #  [1,2],
  #  []
#  ]
#  回溯法
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums==[]:
            return []
        nums.sort()
        out = []
        def backtrack(i,tmp):
            if i > len(nums):
                return
            out.append(tmp)
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]: continue
                backtrack(j+1,tmp+[nums[j]])
        backtrack(0,[])
        return out
