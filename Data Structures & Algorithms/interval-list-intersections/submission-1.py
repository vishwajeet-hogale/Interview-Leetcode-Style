class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        m,n = len (firstList), len(secondList)
        while i < m and j < n:
            if max(firstList[i][0], secondList[j][0]) <= min(firstList[i][1], secondList[j][1]):
               res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            if firstList[i][1] > secondList[j][1]:
                
                j += 1
            elif firstList[i][1] < secondList[j][1]:
                
                i += 1
            else:
                
                i += 1
                j += 1

        return res


        