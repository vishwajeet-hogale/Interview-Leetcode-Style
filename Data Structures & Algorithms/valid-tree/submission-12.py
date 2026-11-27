class Uf:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]                  # fixed: return the root
    def union(self, a, b):
        p_a = self.find(a)
        p_b = self.find(b)
        if p_a != p_b:
            if self.size[p_a] > self.size[p_b]:
                self.parent[p_b] = p_a
                self.size[p_a] += self.size[p_b]
            else:
                self.parent[p_a] = p_b
                self.size[p_b] += self.size[p_a]
            return True
        return False


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:                # fixed: a tree has exactly n - 1 edges
            return False
        uf = Uf(n)
        for s, d in edges:
            if not uf.union(s, d):             # fixed: actually connect, catch cycles
                return False
        return True