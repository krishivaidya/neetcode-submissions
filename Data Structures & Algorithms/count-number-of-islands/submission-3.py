class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        def BFS(i,j):
            visited.add((i,j))
            q.append((i,j))
            while q:
                cur_i, cur_j = q.popleft()
                for di, dj in directions:
                    new_i, new_j = cur_i + di, cur_j + dj 
                    if new_i in range(len(grid)) and new_j in range(len(grid[0])) and grid[new_i][new_j] == "1" and (new_i,new_j) not in visited:
                        visited.add((new_i,new_j))
                        q.append((new_i, new_j))


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count += 1
                    BFS(i,j)
                    
        return count

                
  