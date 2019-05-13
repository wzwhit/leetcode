#  给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#  注意：答案中不可以包含重复的三元组。
#  例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#  满足要求的三元组集合为：
#  [
  #  [-1, 0, 1],
  #  [-1, -1, 2]
#  ]
#1.循环第一个数，找剩下两个数，对撞指针
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#排序方便去重
        out = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] <= 0:
                s = i + 1
                e = n - 1
                while s < e:
                    #print(s,e)
                    if nums[s]+nums[e] == -nums[i]:
                        out.append([nums[i],nums[s],nums[e]])
                        while s < e and nums[s] == nums[s+1]:
                            s += 1
                        s += 1
                    elif nums[s]+nums[e] > -nums[i]:
                        e = e - 1
                    elif nums[s]+nums[e] < -nums[i]:
                        s += 1
        return out

#2.循环第一个数，找剩下两个数，第一题两数之和Hash Table
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] <= 0:
                k = {}
                s = i+1
                while s < n:
                    j = -nums[i] - nums[s]
                    if k.get(j) != None:
                        print(i,s)
                        out.append([nums[i],k.get(j),nums[s]])
                        while s < n-1 and nums[s] == nums[s+1]:
                            s += 1
                    k[nums[s]] = nums[s]
                    s += 1
        return out
