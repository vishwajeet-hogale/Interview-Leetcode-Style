class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lk, ls1, ls2 = len(s3), len(s1), len(s2)
        memo = {}
        def recurse(k, i, j):
            if k >= lk:
                if i >= ls1 and j >= ls2:
                    return True

                return False
            
            
            if (k, i, j) in memo:
                return memo[(k,i,j)]

            res = False
            if i < ls1 and s1[i] == s3[k]:
                res = recurse(k+1, i+1, j)
                
            if j < ls2 and s2[j] == s3[k]:
                res = res or recurse(k+1, i, j+1)
                

            memo[(k,i,j)] = res
            return memo[(k,i,j)]

        return recurse(0,0,0)
