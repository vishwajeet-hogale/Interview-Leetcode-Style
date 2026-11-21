class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x:x[1])
        res = [points[0]]
        cnt = 1
        prevEnd = points[0][1]
        for i, point in enumerate(points):
            if i == 0:
                continue
            if point[0] > prevEnd:
                prevEnd = point[1]
                cnt += 1


                

        return cnt

