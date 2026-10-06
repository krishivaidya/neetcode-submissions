class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        dist[0] = 0 

        adjl = [[] for i in range(n + 1)]
        for u,v,w in times:
            adjl[u].append([w,v])

        minheap = []
        heapq.heappush(minheap, [0,k])
        dist[k] = 0

        while minheap:
            curd, cur = heapq.heappop(minheap)


            for weight, target in adjl[cur]:
                newcost = weight + curd
                if newcost < dist[target]:
                    dist[target] = newcost
                    heapq.heappush(minheap, [newcost, target])

        maxval = 0


        for i in range(1,n + 1):
            if dist[i] == float("inf"):
                return -1
            maxval = max(maxval, dist[i])
        
        return maxval


        
        