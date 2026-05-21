class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["X"] * n for _ in range(n)]

        def check_valid_pos(i, j):
            # Column above
            for r in range(i):
                if board[r][j] == "Q":
                    return False
            # \ diagonal upward
            r, c = i - 1, j - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q": return False
                r -= 1; c -= 1
            # / diagonal upward
            r, c = i - 1, j + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q": return False
                r -= 1; c += 1
            return True

        def solve(i):
            if i == n:
                return 1
            cnt = 0
            for j in range(n):
                if check_valid_pos(i, j):
                    board[i][j] = "Q"
                    cnt += solve(i + 1)
                    board[i][j] = "X"
            return cnt

        return solve(0)