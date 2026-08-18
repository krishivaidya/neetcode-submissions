class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()
        islands = 0

        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visit.add((i,j))

            while q:
                cr, cc = q.popleft()
                for dr,dc in directions:
                    nr,nc = dr + cr, dc + cc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visit and grid[nr][nc] == "1":
                        visit.add((nr,nc))
                        q.append((nr,nc))
            
            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i,j)
                    islands += 1
        return islands
        