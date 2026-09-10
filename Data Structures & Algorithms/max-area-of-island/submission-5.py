class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        q = deque()
        visited = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
                    
                
        def dfs(i,j):
            nonlocal max_area
            count =  1    
            q.append((i,j))
            visited.add((i,j))
        
            while q:
                cur_i, cur_j = q.popleft()
                for di, dj in directions:
                    new_i, new_j = cur_i + di, cur_j + dj 
                    if new_i in range(rows) and new_j in range(cols) and (new_i, new_j) not in visited and grid[new_i][new_j] == 1 :
                        visited.add((new_i, new_j))
                        q.append((new_i, new_j))
                        count += 1

            max_area = max(count, max_area)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)

        return max_area

        


        







        