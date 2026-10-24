class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        wlen = len(word)
        def recurse(widx, i, j, vis):
            print(board[i][j], word[widx])
            if i < 0 or j < 0 or i >= m or j >= n or (i,j) in vis:
                return False
            if widx >= wlen-1:
                return True
            directions = [
                (0, 1),
                (0, -1),
                (-1, 0),
                (1, 0)
            ]
            
            found = False
            vis.add((i,j))
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni,nj) not in vis:
                    if (widx + 1) < wlen and word[widx + 1] == board[ni][nj]:
                        value = recurse(widx + 1, ni, nj, vis)
                        print(f"{board[ni][nj]}:({ni}, {nj}) -> {value}")
                        found = found or value
            vis.remove((i,j))

            return found


        widx = 0
        found = False
        for i in range(m):
            for j in range(n):
                if word[widx] == board[i][j]:
                    print(i,j)
                    vis = set()
                    found = found or recurse(widx, i, j, vis)

        return found

        


