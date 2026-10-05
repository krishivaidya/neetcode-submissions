class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        rows = len(grid)
        cols = len(grid[0])
        area = 0 
        maxarea = 0

        def bfs(i,j):
            nonlocal area 
            area = 0
            q = deque()
            q.append((i,j))
            
            while q:
                curi,curj = q.popleft()
                area += 1
                
                for di,dj in directions:
                    newi, newj = curi + di, curj + dj
                    if newi in range(rows) and newj in range(cols) and grid[newi][newj] == 1:
                        grid[newi][newj] = 0
                        q.append((newi , newj))
                        
                    
                    


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    bfs(i,j)
                    maxarea = max(area, maxarea)

        return maxarea


        
        