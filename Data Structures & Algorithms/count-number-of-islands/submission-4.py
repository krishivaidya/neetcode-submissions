class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        count = 0

        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visit.add((i,j))

            while q:
                curi, curj = q.popleft()
                for di,dj in directions:
                    newi, newj = curi + di, curj + dj
                    if newi in range(rows) and newj in range(cols) and (newi,newj) not in visit and grid[newi][newj] == "1":
                        q.append((newi,newj))
                        visit.add((newi,newj))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i,j)
                    count += 1


        return count

        