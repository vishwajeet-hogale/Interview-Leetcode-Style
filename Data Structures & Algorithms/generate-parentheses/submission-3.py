class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        vis = set()
        def recurse(op, cl, temp):
            nonlocal vis, res
            if op < 0 or cl < 0:
                return
            if op == 0 and cl == 0:
                if temp not in vis:
                    res.append(temp)
                    vis.add(temp)
                return

            
            if op > 0:
                recurse(op - 1, cl, temp + "(")      # can always open if any left
            if cl > op:
                recurse(op, cl - 1, temp + ")")      # can close only if something is open

        recurse(n, n, "")
        return res

        

        