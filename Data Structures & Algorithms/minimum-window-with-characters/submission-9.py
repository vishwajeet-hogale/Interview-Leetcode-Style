from collections import Counter, defaultdict
class Solution:
    def check(self, sdict, tdict):
        for c, cnt in tdict.items():
            if c not in sdict or sdict[c] < cnt:
                return False

        return True

    def minWindow(self, s: str, t: str) -> str:
        tdict = Counter(t)
        sdict = defaultdict(int)
        l, r, n = 0, 0, len(s)
        res = ""
        start, minlen = l, float('inf')
        while r < n:
            sdict[s[r]] += 1
            while l < n and self.check(sdict, tdict):
                if minlen > r - l + 1:
                    start = l
                    minlen = r - l + 1

                sdict[s[l]] -= 1
                if sdict[s[l]] == 0:
                    del sdict[s[l]]
                l += 1

            r += 1

        return "" if minlen == float('inf') else s[start:start+minlen]