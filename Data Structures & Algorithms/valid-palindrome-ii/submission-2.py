class Solution:
    def validPalindrome(self, s: str) -> bool:
        st, end = 0, len(s) - 1
        
        # 1. Find the first mismatch
        while st < end and s[st] == s[end]:
            st += 1
            end -= 1
            
        # If we reached the middle, it's already a palindrome without deletions
        if st >= end:
            return True

        # 2. Path A: Try skipping the left character (st + 1)
        st1, end1 = st + 1, end
        while st1 < end1 and s[st1] == s[end1]:
            st1 += 1
            end1 -= 1
            
        # 3. Path B: Try skipping the right character (end - 1)
        st2, end2 = st, end - 1
        while st2 < end2 and s[st2] == s[end2]:
            st2 += 1
            end2 -= 1
            
        # If either path successfully reaches the middle, it's a valid palindrome
        return st1 >= end1 or st2 >= end2