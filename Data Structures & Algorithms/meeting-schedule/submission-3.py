"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key = lambda x: x.start)

        res = [intervals[0]]
        i, n = 1, len(intervals)
        for i in range(1, n):
            if i < n and intervals[i].start < res[-1].end:
                return False

            else:
                res.append(intervals[i])

        return True

        
