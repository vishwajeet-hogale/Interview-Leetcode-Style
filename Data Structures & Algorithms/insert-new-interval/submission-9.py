class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        res = []
        intervals = sorted(intervals, key = lambda x: x[0])
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        res.append(newInterval)
        while i<n and res[-1][1] >= intervals[i][0]:
            res[-1][0] = min(res[-1][0], intervals[i][0])
            res[-1][1] = max(res[-1][1], intervals[i][1])
            
            i += 1
    
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

