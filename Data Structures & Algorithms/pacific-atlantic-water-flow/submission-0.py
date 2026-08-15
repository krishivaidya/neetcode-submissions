class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()
        rows = len(heights)
        cols = len(heights[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        res = []

        def atlantic_bfs():
            q = deque()
            for j in range(cols):
                q.append((rows - 1,j))
                atlantic.add((rows - 1,j))
            for j in range(rows):
                q.append((j,cols - 1))
                atlantic.add((j,cols - 1))
            while q:
                for i in range(len(q)):
                    cr, cc = q.popleft()
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if nr in range(rows) and nc in range(cols) and (nr,nc) not in atlantic and heights[nr][nc] >= heights[cr][cc]:
                            q.append((nr,nc))
                            atlantic.add((nr,nc))



        def pacific_bfs():
            q = deque()
            for j in range(cols):
                    q.append((0,j))
                    pacific.add((0,j))
            for i in range(rows):
                q.append((i,0))
                pacific.add((i,0))
            while q:
                for i in range(len(q)):
                    cr, cc = q.popleft()
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if nr in range(rows) and nc in range(cols) and (nr,nc) not in pacific and heights[nr][nc] >= heights[cr][cc]:
                            q.append((nr,nc))
                            pacific.add((nr,nc))


        atlantic_bfs()
        pacific_bfs()     
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])    
        return res
        