class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()
        INF = 2147483647
        q = deque()
        dist = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))

        while q:
            for _ in range(len(q)):
                cr, cc = q.popleft()
                grid[cr][cc] = dist
                for dr, dc in directions:
                    nr, nc = cr + dr, cc+ dc 
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visit and grid[nr][nc] == INF:
                        q.append((nr,nc))
                        visit.add((nr,nc))
                
            dist += 1


        