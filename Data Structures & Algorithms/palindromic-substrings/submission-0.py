class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        # mstr = ""
        # mlen = 0
        # Odd case
        res = 0
        for i in range(n):
            curr_idx = i
            l = curr_idx
            r = curr_idx
            # mlen = 1
            # mstr = 
            while 0 <= l < n and 0 <= r < n:
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
        
        # mlen = 1

        for i in range(n):
            curr_idx = i
            l = curr_idx 
            r = curr_idx + 1

            while 0 <= l < n and 0 <= r < n:
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break

        return res