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
        out = []
        def backtrack(k, i, tmp):
            #print(k,i,tmp)
            if i > len(nums):
                return
            if len(tmp) == k:
                if tmp not in out:
                    out.append(tmp)
                return
            for j in range(i, len(nums)):
                backtrack(k, j+1, tmp+[nums[j]])

        for k in range(len(nums)+1):
            backtrack(k,0,[])
        return out
