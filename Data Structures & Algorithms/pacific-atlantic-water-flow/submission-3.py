class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pacific = [["" for _ in range(n)] for _ in range(m)]
        atlantic = [["" for _ in range(n)] for _ in range(m)]

        def dfs(i, j, m, n, ocean, vis):
            if i < 0 or i >= m or j < 0 or j >=n or vis[i][j] != "":
                return

            vis[i][j] = ocean
            # print(vis)
            for di, dj in [
                (0, 1),
                (-1, 0),
                (1, 0),
                (0, -1)
            ]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and vis[ni][nj] == "" and heights[i][j] <= heights[ni][nj]:
                    dfs(ni, nj, m, n, ocean, vis)

            return

        
        # Pacific
        for j in range(n):
            dfs(0, j, m, n, "P", pacific)

        for i in range(m):
            dfs(i, 0, m, n, "P", pacific)

        # Atlantic
        for j in range(n):
            dfs(m-1, j, m, n, "A", atlantic)

        for i in range(m):
            dfs(i, n-1, m, n, "A", atlantic)

        # Compare
        print(pacific)
        print(atlantic)
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == "P" and atlantic[i][j] == "A":
                    res.append((i,j))

        return res


        
        



