class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        col = len(grid[0])
        visited = set()
        islands = 0



        def bfs(i, j):
            q = deque()
            visited.add((i, j))
            q.append((i, j))
            while q:
                r, c = q.popleft()
                directions = [[-1,0],[1,0],[0,1], [0,-1]]
                for dr, dc in directions:
                    newr, newcol = r + dr, c + dc
                    if newr in range(rows) and newcol in range(col) and grid[newr][newcol] == "1" and (newr, newcol) not in visited:
                        visited.add((newr,newcol))
                        q.append((newr,newcol))
        
        
        
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i,j)
                    islands += 1
        
        return islands
        

        
        