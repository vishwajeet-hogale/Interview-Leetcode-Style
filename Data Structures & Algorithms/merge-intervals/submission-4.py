class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: (x[0], x[1]))
        n = len(intervals)
        res = [intervals[0]]

        for i in range(1, n):
            if i < n and intervals[i][0] <= res[-1][1]:
                res[-1][0] = min(intervals[i][0], res[-1][0])
                res[-1][1] = max(intervals[i][1], res[-1][1])
                i += 1
            else:
                res.append(intervals[i])
        return res
        



        