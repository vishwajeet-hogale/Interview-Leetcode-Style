class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        vis = set()
        n = len(candidates)
        res = []
        candidates = sorted(candidates)
        def recurse(i, target, temp):
            nonlocal n, res
            if target == 0:
                key = "".join(str(temp))
                if key not in vis:
                    vis.add(key)
                    res.append(temp)
                return

            if i >= n:
                return
            if candidates[i] > target:
                return
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > target:
                    break
                recurse(j+1, target - candidates[j], temp + [candidates[j]])

            return

        recurse(0, target, [])
        return res

        