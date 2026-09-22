class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        result = []
        for i, j in points:
            d = math.sqrt((i)**2 +(j)**2) * -1
            distances.append((d, [i,j]))
        
        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)

        for d1,d2 in distances:
            result.append(d2)

        return result

        


        