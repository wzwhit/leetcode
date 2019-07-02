#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (42.26%)
# Total Accepted:    25.4K
# Total Submissions: 60.1K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 说明:
#
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
#
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
#
#
class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s = 0
        for i in range(0,n):
            if m > 0:
                if nums2[i] < nums1[0]:
                    nums1[0:0] = [nums2[i]]
                    m += 1
                    nums1.pop()
                else:
                    for j in range(m-1,-1,-1):
                        if nums2[i] >= nums1[j]:
                            nums1[j+1:j+1] = [nums2[i]]
                            m += 1
                            nums1.pop()
                            break
            if m == 0:
                nums1[s:s] = [nums2[i]]
                s += 1
                m += 1
                nums1.pop()

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        c = 0
        n1 = nums1[:]
        while i < m and j < n:
            if n1[i] < nums2[j]:
                nums1[c] = n1[i]
                i += 1
            else:
                nums1[c] = nums2[j]
                j += 1
            c += 1
        for k in range(i,m):
            nums1[c] = n1[k]
            c += 1
        for k in range(j,n):
            nums1[c] = nums2[k]
            c += 1

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()


