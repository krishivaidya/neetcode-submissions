class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visit = set()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visit.add((i,j))
                if grid[i][j] == 1:
                    fresh+= 1


        while q and fresh >0 :
            for _ in range(len(q)):
                cr, cc = q.popleft()
                for nr, nc in directions:
                    r, c = cr + nr, cc + nc
                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c] == 1:
                        q.append((r,c))
                        visit.add((r,c))
                        fresh -= 1
            minutes += 1 

        if fresh > 0:
                return -1
        return minutes 
                
                    
        