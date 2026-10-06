class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        memo = {}

        def dfs(i,j):
            if i == ROWS - 1 and j == COLS - 1:
                return grid[i][j]

            if i not in range(ROWS) or j not in range(COLS):
                return 10000000
            
            if (i,j) in memo:
                return memo[(i,j)]

            memo[i,j] = grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))
            return memo[i,j]

        return dfs(0,0)

        