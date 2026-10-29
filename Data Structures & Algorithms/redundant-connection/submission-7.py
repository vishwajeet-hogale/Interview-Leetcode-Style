class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        # self.rank 
    def find(self, node):
        if self.parent[node] == node:
            return node
        return self.find(self.parent[node])

    def union(self, par_a, par_b):
        if par_a != par_b:
            self.parent[par_b] = par_a
        

        
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n)
        for i, j in edges:
            par_a = uf.find(i)
            par_b = uf.find(j)

            if par_a == par_b:
                return [i,j]

            uf.union(par_a, par_b)

        return [0,0]



        

        