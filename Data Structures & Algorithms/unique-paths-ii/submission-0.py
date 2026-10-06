class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        memo = {}

        def dfs(i, j):
            if i >= ROWS or j >= COLS:
                return 0

            if obstacleGrid[i][j] == 1:
                return 0

            if i == ROWS - 1 and j == COLS - 1:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            down = dfs(i + 1, j)
            right = dfs(i, j + 1)

            memo[(i, j)] = down + right
            return memo[(i, j)]

        return dfs(0, 0)