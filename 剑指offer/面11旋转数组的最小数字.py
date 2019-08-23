# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0

        def midsearch(i, j):
            if i > j:
                return 0
            elif i == j:
                return rotateArray[i]
            mid = (i + j) // 2
            if rotateArray[mid] > rotateArray[i] and rotateArray[mid] > rotateArray[j]:
                i = mid + 1
                return midsearch(i, j)
            elif rotateArray[mid] < rotateArray[i]:
                j = mid
                return midsearch(i, j)
            else:
                return min(midsearch(i, mid), midsearch(mid+1, j))

        return midsearch(0, len(rotateArray) - 1)

if __name__ == "__main__":
    s = Solution()

    date = [4950,4950,4952,4954,4955,4956,4956,4957,4957,4958,4959,4959]
    print(s.minNumberInRotateArray(date))