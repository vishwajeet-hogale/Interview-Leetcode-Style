class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = 1
        prevL, prevR = intervals[0][0], intervals[0][1]
        for l, r in intervals:
            if prevL <= l and prevR >= r:
                continue
            res += 1
            prevL, prevR = l, r

        return res