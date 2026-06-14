from collections import defaultdict, Counter

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, a):
        if self.parent[a] == a:
            return a
        return self.find(self.parent[a])

    def union(self, a, b):
        leader_a = self.find(a)
        leader_b = self.find(b)

        if leader_a != leader_b:
            self.parent[leader_b] = leader_a

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for s, d in edges:
            uf.union(s,d)

        return len({uf.find(i) for i in range(n)})
        