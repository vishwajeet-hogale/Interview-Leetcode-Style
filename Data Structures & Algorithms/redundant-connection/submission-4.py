from collections import defaultdict
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        la = self.find(a)
        lb = self.find(b)

        if la != lb:
            if self.rank[la] > self.rank[lb]:
                self.parent[lb] = la
                return False

            elif self.rank[la] < self.rank[lb]:
                self.parent[la] = lb
                return False
            else:
                self.parent[la] = lb
                self.rank[lb] += 1
                return False

        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for s,d in edges:
            nodes.add(s)
            nodes.add(d)

        n = len(nodes)
        # print(edges)
        uf = UF(n+1)

        for s,d in edges:
            if uf.union(s,d):
                return [s,d]

        return []
            



        