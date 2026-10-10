from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cmap = defaultdict(int)
        l, r, n = 0, 0, len(s)
        mlen = 0
        while r < n:
            cmap[s[r]] += 1
            while sum(cmap.values()) - max(cmap.values()) > k:
                cmap[s[l]] -= 1
                if cmap[s[l]] == 0:
                    del cmap[s[l]]
                l += 1
            mlen = max(mlen, r - l + 1)
            r += 1

        return mlen

        