from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def find_max_char(window):
            s_map = defaultdict(int)
            m_cnt = 0
            m_c = ''
            for c in window:
                s_map[c] += 1
                if s_map[c] > m_cnt:
                    m_c = c
                    m_cnt = s_map[c]

            return m_cnt
                

        window = ""
        s_map = defaultdict(int)
        st, end, n = 0, 0, len(s)
        mlen = 0
        while end < n:
            window += s[end]
            while len(window) - find_max_char(window) > k:
                window = window[1:]
                st += 1
            mlen = max(mlen, end - st + 1)

            end += 1

        return mlen
            
