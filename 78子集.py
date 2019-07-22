#  给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#  说明：解集不能包含重复的子集。
#  示例:
#  输入: nums = [1,2,3]
#  输出:
#  [
  #  [3],
  #  [1],
  #  [2],
  #  [1,2,3],
  #  [1,3],
  #  [2,3],
  #  [1,2],
  #  []
#  ]

#  回溯法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 1:
            return [[]]
        out = []
        def backtrack(res, tmp):
            out.append(tmp)
            if not res:
                return
            for j in range(len(res)):
                backtrack(res[j+1:], tmp+[res[j]])
        backtrack(nums, [])
        return out
