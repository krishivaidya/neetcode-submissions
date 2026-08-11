class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        res = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt(((x - 0)**2) + ((y - 0)**2))
            closest.append([dist, x, y])

        heapq.heapify(closest)
        for _ in range(k):
           mid  = heapq.heappop(closest)
           res.append([mid[1], mid[2]])
        
        return res