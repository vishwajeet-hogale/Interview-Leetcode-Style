class Solution:
    def convert(self, s: str, numRows: int) -> str:
        m, n = numRows, len(s)
        grid = [["" for _ in range(n)] for _ in range(m)]
        beg, end = True, False
        i, j, c = 0, 0, 0
        res = ""
        while c < len(s):
            if beg:

                while i < m and c < len(s):
                    grid[i][j] = s[c]

                    i += 1
                    c += 1
                beg = False
                end = True
                i -= 2 # Because i == m
                j += 1

            elif end:
                while i >= 0 and c < len(s):
                    grid[i][j] = s[c]
                    i -= 1
                    j += 1
                    c += 1

                i += 2 # Because i == -1
                j -= 1 # Because j is gone ahead

                beg = True
                end = False

        for s1 in grid:
            # print(s1)
            res += "".join(s1)
        return res

        
        