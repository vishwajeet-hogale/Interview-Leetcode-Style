class Solution:
    def __init__(self):
        self.board = None
        self.res = []
        self.vis = set()
    def valid(self, i, j, n):
        # Check the column up 
        ci, cj = int(i), int(j)
        while ci >= 0:
            if self.board[ci][cj] == 'Q':
                return False
            ci -= 1
        # CHeck the bottom up diagonal
        ci, cj = int(i), int(j)
        while 0 <= ci < n and 0 <= cj < n:
            if self.board[ci][cj] == 'Q':
                return False
            ci -= 1
            cj += 1

        ci, cj = int(i), int(j)
        while 0 <= ci < n and 0 <= cj < n:
            if self.board[ci][cj] == 'Q':
                return False
            ci -= 1
            cj -= 1

        return True




    def recurse(self, i, n):
        if i >= n :
            sol = ["".join(row) for row in self.board]
            self.res.append(sol)
            return

        for j in range(n):
            if self.valid(i,j,n):
                self.board[i][j] = 'Q'
                self.recurse(i+1, n)
                self.board[i][j] = '.'

        return

    def solveNQueens(self, n: int) -> List[List[str]]:
        # Build the matrix
        self.board = [['.' for _ in range(n)] for _ in range(n)]

        self.recurse(0, n)

        return self.res







        