class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()
        max_area = 0

        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visit.add((i,j))
            count = 1

            while q:
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr,nc = cr + dr, cc + dc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visit and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        visit.add((nr,nc))
                        count += 1
            return count




        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i,j))
        return max_area
        