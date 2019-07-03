#  打乱一个没有重复元素的数组。
#  示例:
#  // 以数字集合 1, 2 和 3 初始化数组。
#  int[] nums = {1,2,3};
#  Solution solution = new Solution(nums);
#  // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
#  solution.shuffle();
#  // 重设数组到它的初始状态[1,2,3]。
#  solution.reset();
#  // 随机返回数组[1,2,3]打乱后的结果。
#  solution.shuffle();

#  暴力法，list.pop()时间是线性的，所以时间复杂度为O(n^2)
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        l = self.nums[:]
        out = []
        while len(l) > 0:
            a = random.randint(0,len(l)-1)
            out.append(l.pop(a))
        return out


#  Fisher-Yates洗牌算法
#  在每次迭代中，生成一个范围在当前下标到数组末尾元素下标之间的随机整数。
#  接下来，将当前元素和随机选出的下标所指的元素互相交换
#  选取下标范围的依据在于每个被摸出的元素都不可能再被摸出来了。
#  此外还有一个需要注意的细节，当前元素是可以和它本身互相交换的
#  否则生成最后的排列组合的概率就不对了。
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        l = self.nums[:]
        for i in range(len(l)):
            a = random.randint(i,len(l)-1)
            l[i], l[a] = l[a], l[i]
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
