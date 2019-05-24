#  给出一个区间的集合，请合并所有重叠的区间。
#  示例 1:
#  输入: [[1,3],[2,6],[8,10],[15,18]]
#  输出: [[1,6],[8,10],[15,18]]
#  解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  示例 2:
#  输入: [[1,4],[4,5]]
#  输出: [[1,5]]
#  解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

#  先按每一项左边界排序，然后开始遍历，后一项的左边界比当前项右边界小则合并，
#  左边界为当前项的左边界，右边界为两项右边界的较大值，否则向后遍历
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        i = 1
        while i < len(intervals):
            #print(i,intervals)
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1:i+1] = [[intervals[i-1][0],max(intervals[i-1][1],intervals[i][1])]]
            else:
                i += 1
        return intervals
