class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, n = 0, len(intervals)
        res = []
        while  i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        res.append(newInterval)

        while i < n and res[-1][1] >= intervals[i][0]:
            res[-1][0] = min(intervals[i][0], res[-1][0])
            res[-1][1] = max(intervals[i][1], res[-1][1])
            i += 1

        while i < n:
            res.append(intervals[i])
            i += 1


        return res
