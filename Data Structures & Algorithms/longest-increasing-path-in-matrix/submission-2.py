class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cache_matrix = [[0]*n for _ in range(m)]
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
                
            if cache_matrix[i][j]:
                return cache_matrix[i][j]


            # vis.add((i,j))
            directions = [
                (0,1),
                (-1, 0),
                (1, 0),
                (0, -1)
            ]
            longest_path = 1
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[i][j]:
                    path = 1 + dfs(nx, ny)
                    longest_path = max(longest_path, path)
            
            cache_matrix[i][j] = longest_path
            return cache_matrix[i][j]

        lip = 0
        for i in range(m):
            for j in range(n):
                if cache_matrix[i][j] == 0:
                    lip = max(lip, dfs(i,j))
        # print(cache_matrix)
        return lip

        

        