from collections import defaultdict, Counter

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self,a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        la = self.find(a)
        lb = self.find(b)

        if la != lb:
            if self.rank[la] < self.rank[lb]:
                self.parent[la] = lb
            elif self.rank[la] > self.rank[lb]:
                self.parent[lb] = la
            else:
                self.parent[la] = lb
                self.rank[lb] += 1
        return

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for s, d in edges:
            uf.union(s,d)
        # print({uf.find(i) for i in range(n)})
        return len({uf.find(i) for i in range(n)})
        