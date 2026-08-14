class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        area = set()
      
        max_area = 0



        def bfs(i,j):
            nonlocal max_area

            q = deque()
            q.append((i,j))
            area.add((i,j))
            visited.add((i,j))
            

            while q:
                pr,pc = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    newr, newc = dr + pr, dc + pc
                    if newr in range(rows) and newc in range(cols) and (newr, newc) not in visited and grid[newr][newc] == 1:
                        visited.add((newr,newc))
                        area.add((newr,newc))
                        
                        q.append((newr,newc))

            if len(area) > max_area:
                max_area = len(area) 
            area.clear()
                    

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    bfs(i,j)
        
        return max_area
        