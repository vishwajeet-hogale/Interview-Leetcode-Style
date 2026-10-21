class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:



        intervals = sorted(intervals, key = lambda x: x[1])
        i, n = 1, len(intervals)
        cnt = 0
        res = [intervals[0]]
        for i in range(1, n):
            if i < n and intervals[i][0] < res[-1][1]:
                cnt += 1
                i += 1
            else:
                res.append(intervals[i])

        return cnt

        

        
        