class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[1])
        print(intervals)
        count, i, n = 0, 1, len(intervals)
        res = [[intervals[0][0], intervals[0][1]]]
        while i < n:
            curr_st, curr_end = intervals[i]
            if curr_st < res[-1][1]:
                count += 1
            else:
                res.append([curr_st, curr_end])
            i += 1
        print(res)
        return count


                    

        