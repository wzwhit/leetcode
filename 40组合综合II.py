#  给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#  candidates 中的每个数字在每个组合中只能使用一次。
#  说明：
    #  所有数字（包括目标数）都是正整数。
    #  解集不能包含重复的组合。
#  示例 1:
#  输入: candidates = [10,1,2,7,6,1,5], target = 8,
#  所求解集为:
#  [
  #  [1, 7],
  #  [1, 2, 5],
  #  [2, 6],
  #  [1, 1, 6]
#  ]
#  示例 2:
#  输入: candidates = [2,5,2,1,2], target = 5,
#  所求解集为:
#  [
  #  [1,2,2],
  #  [5]
#  ]

#  回溯法,去重
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        candidates.sort()
        res = []

        def helper(i, tmp_sum, tmp):
            #print(i,tmp_sum,tmp)
            if tmp_sum == target:
                res.append(tmp)
                return
            if tmp_sum > target or i == len(candidates):
                return
            for j in range(i,len(candidates)):
                if tmp_sum + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                helper(j+1, tmp_sum + candidates[j], tmp + [candidates[j]])

        helper(0, 0, [])
        return res
