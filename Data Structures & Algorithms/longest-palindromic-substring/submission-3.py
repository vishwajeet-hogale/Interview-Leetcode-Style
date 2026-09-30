class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        if n == 1:
            return s
        mstr = ""
        mlen = 0
        # Odd case
        for i in range(n):
            curr_idx = i
            l = curr_idx
            r = curr_idx
            # mlen = 1
            # mstr = 
            while 0 <= l < n and 0 <= r < n:
                if s[l] == s[r]:
                    if mlen < (r - l + 1) :
                        mlen = r - l + 1
                        mstr = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break
        
        # mlen = 1

        for i in range(n):
            curr_idx = i
            l = curr_idx 
            r = curr_idx + 1
            # mlen = 1
            while 0 <= l < n and 0 <= r < n:
                if s[l] == s[r]:
                    if mlen < (r - l + 1) :
                        mlen = r - l + 1
                        mstr = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break

        return mstr
                
        