#  给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#  注意：
#  答案中不可以包含重复的四元组。
#  示例：
#  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#  满足要求的四元组集合为：
#  [
  #  [-1,  0, 0, 1],
  #  [-2, -1, 1, 2],
  #  [-2,  0, 0, 2]
#  ]
#15题三数之和基础上加一个for循环
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 0:
            return []
        nums.sort()
        out = []
        n = len(nums)
        for e in range(n-3):
            if e > 0 and nums[e] == nums[e-1]:
                continue
            for i in range(e+1,n-2):
                if i > e+1 and nums[i] == nums[i-1]:
                    continue
                k = {}
                s = i+1
                while s < n:
                    j = target - nums[e] - nums[i] - nums[s]
                    if k.get(j) != None:
                        out.append([nums[e],nums[i],k.get(j),nums[s]])
                        while s < n-1 and nums[s] == nums[s+1]:
                            s += 1
                    k[nums[s]] = nums[s]
                    s += 1
        return out
