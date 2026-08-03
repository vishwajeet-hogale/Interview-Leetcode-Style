class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[1])
        count, i, n = 0, 1, len(intervals)
        prev_st, prev_end = intervals[0]
        while i < n:
            curr_st, curr_end = intervals[i]
            if curr_st < prev_end:
                count += 1
            else:
                prev_st, prev_end = intervals[i]
            i += 1
        return count