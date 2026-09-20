from collections import defaultdict
from typing import List


class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        leader_a = self.find(a)
        leader_b = self.find(b)

        if leader_a != leader_b:
            if self.rank[leader_a] < self.rank[leader_b]:
                self.parent[leader_a] = leader_b
                # self.rank[leader_b] += self.rank[leader_a]
            elif self.rank[leader_a] > self.rank[leader_b]:
                self.parent[leader_a] = leader_b
                # self.rank[leader_a] += self.rank[leader_b]
            else:
                self.parent[leader_a] = leader_b
                self.rank[leader_b] += 1
            return True

        return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        uf = UF(n)
        for s, d in edges:
            if not uf.union(s,d):
                return False

        return True


        