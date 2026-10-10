from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_map = defaultdict(int)
        mlen = 0
        l, r, n = 0, 0, len(s)
        while r < n:
            character_map[s[r]] += 1

            while character_map[s[r]] > 1:
                character_map[s[l]] -= 1
                if character_map[s[l]] == 0:
                    del character_map[s[l]]

                l += 1
            mlen = max(mlen, r - l + 1)
            r += 1

        return mlen
                

        