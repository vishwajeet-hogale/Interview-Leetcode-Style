from collections import Counter, defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegree = [0 for _ in range(n+1)]
        ad_list = defaultdict(list)
        for s,d in trust:
            inDegree[d] += 1
            ad_list[s] = d
        
        if n - 1 not in inDegree:
            return -1
        judge = inDegree.index(n-1)
        if judge not in ad_list:
            return judge

        return -1
        