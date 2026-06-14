from collections import defaultdict
from typing import List


class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, a):
        if self.parent[a] == a:
            return a
        return self.find(self.parent[a])

    
        

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        uf = UF(n=n)
        for s, d in edges:
            leader_a = uf.find(s)
            leader_b = uf.find(d)

            if leader_a == leader_b:
                return False
            uf.parent[leader_b] = leader_a
            
        print(uf.parent)
        return True