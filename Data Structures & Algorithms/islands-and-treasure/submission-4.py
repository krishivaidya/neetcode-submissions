class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append(((i,j),0))

        while q:
            (curi, curj), steps = q.popleft()

            for di,dj in directions:
                newi, newj = di + curi, dj + curj

                if newi in range(rows) and newj in range(cols) and grid[newi][newj] == 2147483647:
                    grid[newi][newj] = steps + 1
                    q.append(((newi,newj),steps + 1))


        

            


                

        