#  给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#  示例 1:
#  输入: nums = [1,1,1,2,2,3], k = 2
#  输出: [1,2]
#  示例 2:
#  输入: nums = [1], k = 1
#  输出: [1]
#  说明：
    #  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
    #  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

#  先用一个hashtable记录每种数的频率，然后按频率双路快排，时间复杂度O(n+nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 1 or k < 1:
            return []
        #  计数O(n)
        hashtable = {}
        for i in nums:
            if hashtable.get(i):
                hashtable[i] += 1
            else:
                hashtable[i] = 1
        f = []
        n = []
        for i in hashtable:
            n.append(i)
            f.append(hashtable[i])
        #  双路快排O(nlogn)
        def Quicksort(f, n):
            if len(f) <= 1:
                return
            def partition(f, l, r):
                k = l
                while l < r:
                    while l < r and f[r] >= f[k]:
                        r -= 1
                    while l < r and f[l] <= f[k]:
                        l += 1
                    f[l], f[r] = f[r], f[l]
                    n[l], n[r] = n[r], n[l]
                f[l], f[k] = f[k], f[l]
                n[l], n[k] = n[k], n[l]
                return l
            def qsort(f, l, r):
                if l >= r:return
                mid = partition(f, l, r)
                qsort(f, l, mid-1)
                qsort(f, mid+1, r)
                # print(f,n)
            qsort(f, 0, len(f)-1)

        Quicksort(f,n)
        # print(f,n)
        return n[-1:-k-1:-1]
